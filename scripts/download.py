#!/usr/bin/env python3
import os
import sys
import http.server
import subprocess
import json

#script to download sample cases.

def listen(*, timeout=None):
    print("starting HTTP Server on port 10046...")
    json_data = None
    class CompetitiveCompanionHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            nonlocal json_data
            json_data = json.load(self.rfile)
            json_data = json.dumps(json_data, indent=4)

    with http.server.HTTPServer(('127.0.0.1', 10046), CompetitiveCompanionHandler) as server:
        server.timeout = timeout
        server.handle_request()
    if json_data is None:
        print("failed")
    with open("tests.json", "w") as f:
        f.write(json_data)
    print(json_data)
    return json_data

listen()
