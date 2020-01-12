from picamera import PiCamera
import time

output = "/home/pi/flask-rest-api/video.mjpeg"

camera = PiCamera()
camera.rotation = 180
camera.start_recording(output, format='mjpeg')
time.sleep(5)
camera.stop_recording()
