#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
curl -sLw "%{http_code}" "$1" -o /dev/null | {
    read code
    # Check if the status code is 200 before displaying the body
    if [ "$code" -eq 200 ]; then
        curl -sL "$1"
    fi
}
