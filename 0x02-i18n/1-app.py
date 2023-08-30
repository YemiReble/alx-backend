#!/usr/bin/env python3
""" A flask web application for translation
"""


from flask import Flask, render_template, request
from flask_babel import Babel, format_datetime
from flask_babel import _
import datetime
import pytz


app = Flask(__name__)
app.strict_slashes = False
babel = Babel(app)


class Config():
    """ Language Translation Class """
    LANGUAGES = ["en", "fr"]
    locale = "en"
    timezone = "UTC"
    time_zone = datetime.datetime.now(pytz.utc)
    # babel = Babel(app)


@app.route("/")
def index_one():
    """ App Index page """
    locale = Config.locale
    time_zone = format_datetime(Config.time_zone)
    return render_template("1-index.html", locale=locale, time_zone=time_zone)


if __name__ == "__main__":
    app.run(port=5050)
