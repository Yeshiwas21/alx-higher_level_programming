#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -sL -w "%{http_code}" "$1" -o /dev/null | {
    read code
    if [ "$code" -eq 200 ]; then
        curl -s "$1"
    fi
}
