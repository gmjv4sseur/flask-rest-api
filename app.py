from flask import Flask, jsonify, request, make_response
import jwt

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
    app.run(debug=True)