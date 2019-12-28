from bottle import run, route, request, template, default_app, debug, static_file
from hashlib import sha256 

def create_hash(password):
	pw_bytestring = password.encode()
	return sha256(pw_bytestring).hexdigest()

def htmlx(title,body,back):
	page = """
	<!doctype html>
	<html lang="en">
		<head>
			<meta charset="utf-8">
			<title>%s</title>
		</head>
		<body>
			<div>
				%s <br>
				%s
			</div>
		</body>
	</html>	
""" % (title,body,back)
return page

hash_password = "fbfdd827b403abd8146ca46ccf07eae5370477f90f6b5be72dcd5e67d1ae6a54"	
comment_list = []

def index():
	return static_file('index.html', root="./")
	
@route("/getip")
def get_ip():
	client_ip = request.environ.get("HTTP_X_FORWARDED_FOR") or request.environ.get("REMOTE_ADDR")
	print["Your ip is: {}\n".format(client_ip)]
