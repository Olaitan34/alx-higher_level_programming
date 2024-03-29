#!/usr/bin/python3

"""
Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)
"""

   
if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    val = {'email': sys.argv[2]}
    par = urllib.parse.urlencode(val)
    par = par.encode('ascii')
    request = urllib.request.Request(url, par)
    with urllib.request.urlopen(request) as res:
        resV = res.read()
        print(resV.decode('utf-8'))
