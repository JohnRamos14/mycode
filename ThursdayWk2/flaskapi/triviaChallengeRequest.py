#!/usr/bin/env python3

import requests
from pprint import pprint

URL = "http://127.0.0.1:224/"

resp = requests.get(URL).json()

pprint(resp)
