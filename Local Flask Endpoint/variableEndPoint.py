import os, json, requests
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

# String is default type
@app.route('/echo/<aString>')
def show_user_profile(aString):
    return 'You input: %s' % aString

"""
| TYPES
| string    accepts any text without a slash (the default)
| int       accepts integers
| float     like int but for floating point values
| path      like the default but also accepts slashes
| any       matches one of the items provided
| uuid      accepts UUID strings
"""
@app.route('/page/<int:pageNum>')
def show_post(pageNum):
    return 'This is page: %d' % pageNum

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)