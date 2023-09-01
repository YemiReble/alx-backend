#!/usr/bin/env python3
""" A flask web application for translation
"""


from flask import Flask, render_template, request
from flask_babel import Babel, format_datetime, current_app
from flask_babel import _
# from babel import localeselector
import datetime
import pytz


app = Flask(__name__)
app.strict_slashes = False
babel = Babel(app)


class Config():
    """ Configuration Class """

    LANGUAGES = ['en', 'fr']
    log = {'en': 'English', 'fr': 'French'}

    locale = 'en'
    timezone = 'UTC'
    time_zone = datetime.datetime.now(pytz.utc)
    # babel = Babel(app)


@app.route("/")
def index_one():
    """ App Index page """

    locale = Config.locale
    time_zone = format_datetime(Config.time_zone)
    return render_template("2-index.html", locale=locale, time_zone=time_zone)


@babel.localeselector
def get_locale():
    """
    Get the best match for the user's locale from the supported languages.
    """
    LANG = Config.LANGUAGES
    LANGUAGES = {'en': 'English', 'fr': 'French'}
    # for la in LANG:
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
    # accepted_lang = request.accept_languages.split(',')
    # lang = localeselector.best_match(accepted_lang, Config.LANGUAGES)
    # return lang

# @babel.localeselector
# def get_locale():
#    """ Get Locale Function """
#    dic_lang = Config.LANGUAGES
#    # for lan in lang:
#    reqst_lang = request.accept_languages.best_match(dic_lang)
#    lang = reqst_lang[0]
#    if lang not in reqst_lang:
#        lang = Config.locale
#
#    return current_app.config['LOCALE']


if __name__ == "__main__":
    app.run(port=5050)
