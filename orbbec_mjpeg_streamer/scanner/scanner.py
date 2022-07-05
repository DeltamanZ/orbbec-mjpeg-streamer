import asyncio
import logging
from operator import truediv
import cv2
import numpy


logger = logging.getLogger('orbbec-mjpeg-streamer')


class Scanner:
    def __init__(self, video_params: dict):
        self._video_params = video_params

    async def init_device(self):
        self._camera = cv2.VideoCapture(0)
        self._camera.set(3, self._video_params["width"])
        self._camera.set(4, self._video_params["height"])
        self._camera.set(5, self._video_params["fps"])
        self._camera.set(11, self._video_params["contrast"])
        self._camera.set(12, self._video_params["saturation"])
        self._camera.set(13, self._video_params["hue"])
        self._camera.set(14, self._video_params["gain"])
        self._camera.set(17, self._video_params["white_balance_temperature"])
        self._camera.set(20, self._video_params["sharpness"])
        self._camera.set(32, self._video_params["backlight_compensation"])
        self._camera.set(21, self._video_params["exposure_auto"])        
        assert self._camera.isOpened()
    
    async def image_grabber(self, app):
        while True:
            result, frame = self._camera.read()
            if result:
                frame = cv2.imencode('.jpeg', frame)[1].tobytes()        
                app["frame"] = b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
            await asyncio.sleep(1 / self._video_params["fps"])
