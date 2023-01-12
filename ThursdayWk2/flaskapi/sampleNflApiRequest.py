#!/usr/bin/env python3
"""Request practice"""

import requests
import json
from pprint import pprint

URL = "http://127.0.0.1:2224/"

new_team = {
            "team_name": "Bills",
            "state": "NY",
            "division": "AFC"
            }

new_team = json.dumps(new_team)

resp = requests.post(URL, json=new_team)

pprint(resp.json())
