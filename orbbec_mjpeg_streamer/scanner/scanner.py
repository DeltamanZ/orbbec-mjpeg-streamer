import logging


logger = logging.getLogger('orbbec-mjpeg-streamer')


class Scanner:

    def __init__(self, video_params: dict):
        self._video_params = video_params

    async def init_device(self):
        # TODO: метод, в котором реализуем подключение к камере с помощью библиотеки opencv-python
        return

    async def image_grabber(self, app):
        # TODO: метод, в котором мы получаем кадры с камеры и сохраняем их в переменную app['frame'] в формате jpg
        pass
