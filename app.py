import subprocess, datetime, time, sys

try:
	import json
except ImportError:
	import simplejson as json

try:
	import pythonwhois
except ImportError:
	print "pythonwhois is not installed!"
	exit(1)

try:
	import pymongo
except ImportError:
	print "pymongo is not installed!"
	exit(1)

from flask import Flask, request, render_template, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = "er4988n439h981359n5n9n5954b0fsdfkjglqrekjt0314njn"
app.debug=True
db = pymongo.Connection()['crytowhois']

def format_date(dates):
	if dates is None:
		return None
	else:
		return dates[0].isoformat()

def get_first(options):
	if options is None:
		return None
	else:
		return options[0]

def unicodedammit(input_string):
	if isinstance(input_string, str):
		return input_string.decode('utf-8')
	else:
		return input_string

def whois(domain):
	raw, result = pythonwhois.whois(domain)
	
	if result['creation_date'] is None and result['expiration_date'] is None and result['registrar'] is None and result['name_servers'] is None:
		return None
	else:
		creation_date = format_date(result['creation_date'])
		expiration_date = format_date(result['expiration_date'])
		updated_date = format_date(result['updated_date'])
		registrar = get_first(result['registrar'])
		whois_server = get_first(result['whois_server'])
		emails = result['emails']
		nameservers = result['name_servers']
		
		return unicodedammit(raw), {
			'creation_date': unicodedammit(creation_date),
			'expiration_date': unicodedammit(expiration_date),
			'updated_date': unicodedammit(updated_date),
			'registrar': unicodedammit(registrar),
			'whois_server': unicodedammit(whois_server),
			'emails': unicodedammit(emails),
			'nameservers': unicodedammit(nameservers)
		}

@app.route('/', methods=["GET"])
def home():
	return render_template("home.tpl")

def find_whois(domain):
	db_results = db['responses'].find_one({'domain': domain})
	
	if db_results is not None:
		try:
			raw = db_results['raw']
		except KeyError:
			raw = None
		
		return (db_results['timestamp'], db_results['response'], raw)
	else:
		returned = whois(domain)
		
		if returned is not None:
			raw, result = returned
			
			db['responses'].insert({
				'domain': domain,
				'response': result,
				'timestamp': time.time(),
				'raw': raw
			})
			
			return (time.time(), result, raw)
		else:
			return (time.time(), None, None)

@app.route('/query', methods=["POST"])
def query():
	try:
		domain = request.form['domain']
		
		if domain == "":
			flash("You did not enter a domain.")
			return render_template("home.tpl")
		else:
			return redirect(url_for('query_html', domain=domain))
	except KeyError, e:
		flash("You did not specify a domain.")
		return render_template("home.tpl")

@app.route('/query/html/<domain>', methods=["GET"])
def query_html(domain):
	retrieval_date, result, raw = find_whois(domain)
	
	if result is None:
		flash("The specified domain does not exist.")
		return render_template("home.tpl"), 404
	else:
		retrieval_timestamp = datetime.datetime.fromtimestamp(int(retrieval_date))
		
		return render_template("result.tpl", domain=domain, retrieval_date=retrieval_timestamp.isoformat(), raw=raw, **result)


@app.route('/query/json/<domain>', methods=["GET"])
def query_json(domain):
	if domain is not None:
		retrieval_date, result, raw = find_whois(domain)
		
		if result is not None:
			result['retrieval_date'] = int(retrieval_date)
			result['raw_response'] = raw
			return json.dumps(result)
		else:
			return json.dumps(None)
	else:
		return json.dumps(None)

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=1234, debug=True)
