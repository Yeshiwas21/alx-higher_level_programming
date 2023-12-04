#!/usr/bin/python3
"""Takes in a URL, sends a request, and displays the body of the response.
   If the HTTP status code is greater than or equal to 400, print an error message.
"""

import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
    print(response.text)
except requests.exceptions.HTTPError as err:
    print("Error code:", response.status_code)
