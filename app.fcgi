#!/usr/local/bin/python
from flup.server.fcgi import WSGIServer
from app import app
from werkzeug.contrib.fixers import LighttpdCGIRootFix

if __name__ == '__main__':
	WSGIServer(LighttpdCGIRootFix(app)).run()
