import asyncio
from importlib.metadata import metadata
from time import time
from aiohttp import request
from aiohttp_jsonrpc import handler
from orbbec_mjpeg_streamer.database.Database import add_frame, get_frames_count


class RPC(handler.JSONRPCView):
    async def rpc_saveFace(self):
        start_time = time()
        while time() - start_time < 10:
            if self.request.app["face_found"] == True:
                frame = self.request.app["last_frame"]
                await add_frame(frame)
                return "Picture has been taken"
            await asyncio.sleep(0.1)
        return "Timeout"
    
    async def rpc_getFacesCount(self):
        return await get_frames_count()