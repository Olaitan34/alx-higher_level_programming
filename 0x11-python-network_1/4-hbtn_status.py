#!/usr/bin/python3

"""
Python script that fetches
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests

    url = requests.get("https://alx-intranet.hbtn.io/status")
    text = res.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
