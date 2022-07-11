from datetime import datetime
from importlib.metadata import metadata
from time import time
from aiopg.sa import create_engine
import sqlalchemy as sa 


metadata = sa.MetaData()

picture_table = sa.Table("picture", metadata, 
                    sa.Column("id", sa.Integer, primary_key=True),
                    sa.Column("frame", sa.LargeBinary),
                    sa.Column("taken", sa.TIMESTAMP))

async def add_frame(frame):
    engine = await create_engine(user="postgres", password="postgres", host="127.0.0.1", port=5432, database="people")
    with (await engine) as conn:
        await conn.execute(picture_table.insert().values(frame=frame, taken=datetime.now().isoformat()))

async def get_frames_count() -> int:
    engine = await create_engine(user="postgres", password="postgres", host="127.0.0.1", port=5432, database="people")
    timestamps = []
    result = 0
    with (await engine) as conn:
        async for row in conn.execute(picture_table.select()):
            timestamps.append(row.taken)
            result += 1
    return {"count": result, "timestamps": timestamps}
