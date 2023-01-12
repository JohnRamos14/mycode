#!/usr/bin/env python3
""" Demo: receiving JSON
    from my sample nfl api"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json

app = Flask(__name__)

playoff_data = [{
    "team_name": "Chiefs",
    "state": "MO",
    "division": "AFC"
    }]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
            data = json.loads(data)
            team_name = data["team_name"]
            state = data["state"]
            division = data["division"]
            playoff_data.append({"team_name":team_name, "state": state, "division": division})

    return jsonify(playoff_data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=2224)

