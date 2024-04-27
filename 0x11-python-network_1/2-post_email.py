#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        data = parse.urlencode({"email": email}).encode("ascii")
        with request.urlopen(url, data) as response:
            response_body = response.read().decode("utf-8")
            print(response_body)
