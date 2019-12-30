import os
from bottle import *
from hashlib import sha256
from pathlib import Path
user_password = "fbfdd827b403abd8146ca46ccf07eae5370477f90f6b5be72dcd5e67d1ae6a54"
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
ips = []
@route("/static/<filename>")
def static_content(filename):
    return static_file(filename, root='./static')
def add_ip():
    global ips
    global new_ip
    if new_ip in ips:
        ips[new_ip] += 1
    else:
        ips[new_ip] = 1
def home():
    return Path("index.html").read_text()

def get_edu():
    global new_ip
    new_ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    global ips
    add_ip()
    return template('index2', iplist=ips)
    return Path("index1.html").read_text()
def create_app():
    app = Bottle()
    app.route("/", "GET", home)
    app.route("/index1.html", "GET", get_edu)
    app.route("/static/<filepath:path>", "GET", static_content)
    return app

ips = {}
application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
