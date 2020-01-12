from picamera import PiCamera
from time import time

output = "/home/pi/flask-rest-api/video.mp4"

camera = PiCamera()
camera.rotation = 180
camera.start_recording(output, format='mp4')
time.sleep(5)
camera.stop_recording()