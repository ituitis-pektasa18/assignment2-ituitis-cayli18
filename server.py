import os
from bottle import *
from hashlib import sha256
from pathlib import Path
user_password = "fbfdd827b403abd8146ca46ccf07eae5370477f90f6b5be72dcd5e67d1ae6a54"
def create_hash(password):
    pw_bytestring = password.encode()
    return sha256(pw_bytestring).hexdigest()
ips = []
def add_ip(a,b):
    global ips
    if a in b:
        a[b] += 1
    else:
        a[b] = 1
def home():
    new_ip = request.headers.get("X-Forwarded-For", "127.0.0.1")
    global ips
    add_ip(new_ip,ips)
    tableContent ="""
    <html>
        <body>  
            <tr>
                <td>%s (new_ip) %s </td>
                <td>%s (ips[new_ip] %s </td>
            </tr>
        </body>
    </html>
    """
    return tableContent
def get_edu():
    return Path("/index1.html")
def create_app():
    app = Bottle()
    app.route("/", "GET", home)
    app.route("/login", "GET", get_edu)

    return app
application = create_app()
application.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
