<!doctype html>
<html>
	<head>
		<title>Cryto WHOIS</title>
		<link rel="stylesheet" href="/static/style.css">
		<link href='http://fonts.googleapis.com/css?family=Orienta' rel='stylesheet' type='text/css'>
		<link href='http://fonts.googleapis.com/css?family=Source+Sans+Pro:400,700' rel='stylesheet' type='text/css'>
	</head>
	<body>
		<div id="header">
			<h1>Cryto WHOIS</h1>
			Free and unlimited WHOIS lookups and JSON API
		</div>
		{% with messages = get_flashed_messages() %}
			{% if messages %}
				<ul id="flashes">
					{% for message in messages %}
						<li>{{ message }}</li>
					{% endfor %}
				</ul>
			{% endif %}
		{% endwith %}
		<div id="contents">
			<form id="whois_form" method="post" action="/query">
				<label for="domain_input">Look up a domain:</label>
				<input id="domain_input" type="text" name="domain">
				<button type="submit" name="submit">WHOIS!</button>
			</form>
			{% block body %}
				It would seem the page you requested was not found.
			{% endblock %}
		</div>
		<div id="footer">
			<strong>Hi. Thanks for using Cryto WHOIS.</strong> I live off donations, so any financial contribution would be <a href="http://cryto.net/~joepie91/donate.html">very welcome</a>! Source code for this site is coming soon.
		</div>
	</body>
</html>
