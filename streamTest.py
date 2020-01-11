import picamera

with picamera.PiCamera() as camera:
    with picamera.PiCameraCircularIO(camera,seconds=10) as stream:
        camera.start_recording(stream, format='h264')
        camera.wait_recording(10)
        camera.stop_recording()
