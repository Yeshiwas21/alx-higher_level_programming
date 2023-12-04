#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    content = response.read()
    print("Body response:")
    print("    - type: {}".format(type(content)))
    print("    - content: {}".format(content))
    print("    - utf8 content: {}".format(content.decode('utf-8')))

