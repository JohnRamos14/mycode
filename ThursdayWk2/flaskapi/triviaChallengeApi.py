#!/usr/bin//env python3
"""Lab 103 Challenge
    Flask trivia API"""

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template

app = Flask(__name__)

URL = "https://opentdb.com/api.php?amount=5&category=28&difficulty=easy&type=multiple"

@app.route("/")
def index():
    response = request.get(URL)
    data = response.jsonify(response)
    questions = data["results"]
    return render_template("trivia.html", question=questions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
