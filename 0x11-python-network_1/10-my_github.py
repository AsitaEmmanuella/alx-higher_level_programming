#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token = sys.argv[2]
        auth = HTTPBasicAuth(username, token)
        url = "https://api.github.com/user"
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        else:
            print("None")
