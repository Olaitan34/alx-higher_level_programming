#!/usr/bin/python3

"""THIS SCRIPT IS TO FETCH AN URL"""

import urllib.request


if __name__ == "__main__":
  request = urllib.request.Request("https://alx-intranet.hbtn.io/status")
  with urllib.request.urlopen(request) as van:
      body = van.read()
      print("Body response:")
      print("\t- content: {}".format(type(body)))
      print("\t- uft8 content: {}".format(body.decode("uft-8")))
