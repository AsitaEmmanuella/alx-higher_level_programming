#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable in the response header
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        request_id = response.headers.get("X-Request-Id")
        print(request_id)
