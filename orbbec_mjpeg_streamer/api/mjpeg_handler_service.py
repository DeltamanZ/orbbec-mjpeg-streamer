from math import dist
from aiohttp import web, MultipartWriter
from aiohttp_cors import CorsViewMixin
from asyncore import write
from m7_aiohttp.util.logged import logged
import logging
import asyncio


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

    @logged(logger)
    async def mjpeg_handler_depth(self, request):
        response = web.StreamResponse()
        response.content_type = 'multipart/x-mixed-replace; boundary=frame'
        await response.prepare(request)
        while True:
            await response.write(request.app["depth"])

    @logged(logger):
    async def mjpeg_handler_min_distance(self, request):
        response = web.StreamResponse()
        response.content_type = 'multipart/x-mixed-replace; boundary=border'
        await response.prepare(request)
        while True:
            distance = request.app["min_distance"]
            await response.write(f"--border\r\nContent-Type: text/plain\r\n\r\n{distance}\r\n".encode("utf-8"))
            await asyncio.sleep(1)
