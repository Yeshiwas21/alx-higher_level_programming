#!/bin/bash
# Get the response body for a given URL for 200 status code responses.
response=$(curl -sL -w "%{http_code}" "$1")
if [[ $response == *"200"* ]]; then
    echo "$response" | sed -n '/^\s*$/,$p' | tail -n +2
fi
