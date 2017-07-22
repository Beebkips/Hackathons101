import os, json, requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route("/endpoint")
def start():
    json = {'test' : 'response'}
    return jsonify(json)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # go to localhost:5000/endpoint