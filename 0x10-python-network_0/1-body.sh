#!/bin/bash
# This script takes in a URL, sends a GET request, and displays the body of the response for a 200 status code
curl -sL "$1" -w "%{http_code}" -o /dev/null | {
    read code
    if [ "$code" -eq 200 ]; then
        curl -sL "$1"
    fi
}
