<!DOCTYPE html>
<html>
  <head>
	<title>Log on to clear the page</title>
  </head>
  <body>
	
	<div>
		<form action="/password" method="post">
			{{info}}
			<h1>Password here!</h1>
			<div class="textbox">
				<input type="password" placeholder="Password" name="pw" value="">
			</div>
			<input type="submit" value="Enter">
		</form>
	</div>
	<div>
		<a href="/index1.html"><h3>Back to index</h3></a>
	</div>
  </body>
</html>

