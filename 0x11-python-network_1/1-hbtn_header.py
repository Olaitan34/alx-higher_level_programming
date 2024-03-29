#!/usr/bin/python3

"""script that send request and display the value of the x-Request-Id"""

import urllib.request
import sys




if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as van:
        print(dict(response.headers).get("X-Request-Id"))
