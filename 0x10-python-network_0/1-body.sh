#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code
response=$(curl -sL -w "%{http_code}" "$1")
if [[ $response == *"200"* ]]; then
    echo "$response" | sed -n '/^\s*$/,$p' | tail -n +2
fi
