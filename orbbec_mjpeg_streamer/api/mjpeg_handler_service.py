import logging

from aiohttp_cors import CorsViewMixin
from m7_aiohttp.util.logged import logged


logger = logging.getLogger('orbbec-mjpeg-streamer')


class MjpegHandlerService(CorsViewMixin):

    @logged(logger)
    async def mjpeg_handler_rgb(self, request):
        # TODO: реализуем метод, генерирующий mjpeg-поток на основе кадров из переменной app['frame']
        pass
