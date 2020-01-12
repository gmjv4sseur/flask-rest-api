from picamera import PiCamera
import time

output = "/home/pi/flask-rest-api/video.h264"

camera = PiCamera()
camera.rotation = 180
camera.start_recording(output, format='h264')
time.sleep(5)
camera.stop_recording()
