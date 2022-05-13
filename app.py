import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/encrypt", methods=['POST', "GET"])
def hello_world():
    if request.method == "POST":
        req = json.loads(request.data)
        print(req["plainText"])
    return


if __name__ == '__main__':
    app.run(debug=True)
