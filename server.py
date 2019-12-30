import os
from bottle import *
from hashlib import sha256
from pathlib import Path
user_password = "fbfdd827b403abd8146ca46ccf07eae5370477f90f6b5be72dcd5e67d1ae6a54"
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
ips = []

def static_content(filepath):
    return static_file(filepath, root='./')
def add_ip():
    global ips
    global new_ip
    if new_ip in ips:
        ips[new_ip] += 1
    else:
        ips[new_ip] = 1
def home():
    global new_ip
    new_ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    global ips
    add_ip()
    return template('index2', iplist=ips)
def get_edu():
    return Path("index1.html").read_text()
def create_app():
    app = Bottle()
    app.route("/", "GET", home)
    app.route("/login", "GET", get_edu)
    return app

ips = {}
application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
