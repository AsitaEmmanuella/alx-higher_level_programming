#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8). It also
manages HTTPError exceptions and prints the error code.
"""
import sys
from urllib import request, error

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        try:
            with request.urlopen(url) as response:
                response_body = response.read().decode("utf-8")
                print(response_body)
        except error.HTTPError as e:
            print("Error code:", e.code)
