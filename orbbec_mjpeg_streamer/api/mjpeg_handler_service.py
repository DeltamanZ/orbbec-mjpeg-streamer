from aiohttp import web, MultipartWriter
from aiohttp_cors import CorsViewMixin
from asyncore import write
from m7_aiohttp.util.logged import logged
import logging


logger = logging.getLogger('orbbec-mjpeg-streamer')


class MjpegHandlerService(CorsViewMixin):
    def __init__(self) -> None:
        super().__init__()

    @logged(logger)
    async def mjpeg_handler_rgb(self, request):
        response = web.StreamResponse()
        response.content_type = 'multipart/x-mixed-replace; boundary=frame'
        await response.prepare(request)
        while True:
            await response.write(request.app["frame"])