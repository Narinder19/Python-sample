import math
import os
import sys
import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    print("Hello World")


r = requests.get("https://google.com")
print(r.status_code)

