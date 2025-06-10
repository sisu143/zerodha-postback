from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello from Render!", 200

@app.route('/postback', methods=['POST'])
def postback():
    data = request.json
    print("Received Postback:", data)
    return "OK", 200
