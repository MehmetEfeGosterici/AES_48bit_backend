import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from encrypt import plainTextToCipherText
from keygen import keyGen

app = Flask(__name__)
CORS(app)

firstBlock = []
afterSubBytes = []
AfterShiftRows = []
afterMixColumns = []

@app.route("/")
def hello():
    return "hello"

@app.route("/encrypt", methods=['POST', "GET"])
def hello_world():
    if request.method == "POST":
        req = json.loads(request.data)["plainText"]
        keys = keyGen()
        response = plainTextToCipherText(req,keys,firstBlock,afterSubBytes,AfterShiftRows,afterMixColumns)
        #print(response)
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
