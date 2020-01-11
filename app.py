from flask import Flask, jsonify, request, make_response
import jwt
from picamera import PiCamera

app = Flask(__name__)

@app.route('/unprotected')
def unprotected():
    return ''

@app.route('/protected')
def protected():
    return ''

@app.route('/login')
def login():
    auth = request.authorization
    if auth and auth.password == 'password':
        return ''
    return make_response('Error with auth', 401, {'WWW-Authenticate' : 'Basic realm="Login required"'})

if __name__ =='__main__':
    #app.run(host="0.0.0.0",debug=True)
    camera = PiCamera()
    camera.rotation = 180
    camera.capture('/home/pi/flask-rest-api/pictures/image.jpg')

