#!/usr/bin/env python3

import webbrowser
import http.server
import socketserver
import threading

PORT = 8000
DIRECTORY = __file__[:-6] + 'firebird.w3spaces.com/'

class Handler(http.server.SimpleHTTPRequestHandler):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, directory=DIRECTORY, **kwargs)
		
	
def serve():
	with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
		print("serving at port", PORT)
		httpd.serve_forever()

threading.Thread(target=serve).start()
webbrowser.open('http://127.0.0.1:8000/')