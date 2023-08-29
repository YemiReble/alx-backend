#!/usr/bin/env python3
""" A flask web application for translation
"""


from flask import Flask, render_template
from flask_babel import Babel
import datetime
import pytz


app = Flask(__name__)
app.strict_slashes = False
bable = Babel(app)


class Config():
    """ Language Translation Class """
    LANGUAGES = ["en", "fr"]
    locale = "en"
    time_zone = datetime.datetime.now(pytz.utc)

@app.route("/")
def index():
    """ App Index page """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port=5050)
