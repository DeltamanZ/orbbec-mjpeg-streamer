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

    @logged(logger)
    async def mjpeg_handler_min_distance(self, request):
        resp = web.StreamResponse(status=200, 
                              reason='OK', 
                              headers={'Content-Type': 'text/html'})
        await resp.prepare(request)
        await resp.write(f"<html><body id=\"test\">Test</body></html>".encode("cp1251"))
        while True:
            dist = request.app["min_distance"]
            await resp.write(f"<script>if (test === undefined) var test = document.getElementById(\"test\"); test.innerText = \"{dist}\" </script>".encode("utf-8"))
            await resp.drain()
            await asyncio.sleep(1)
        # return web.Response(text=request.app["min_distance"])  
