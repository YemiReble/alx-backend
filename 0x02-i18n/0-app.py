#!/usr/bin/env python3
""" A flask web application for translation
"""


from flask import Flask, render_template


app = Flask(__name__)
app.strict_slashes = False


@app.route("/")
def index():
    """ App Index page """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port=5050)
