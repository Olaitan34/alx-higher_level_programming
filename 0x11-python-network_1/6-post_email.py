#!/usr/bin/python3

"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as
a parameter, and finally displays the body of the response.
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.arg[1]
    val = {"email": sys.argv[2]}
 
    with requests.post(url, data = val) as resp:
        print(resp.text)
