#!/usr/bin/env python3

# author: greyshell

import os
import random
import string
from flask import Flask, render_template
from flask import request
from web.sqli.models import *
from mysql_db import MySQLdb

templates_path = os.path.abspath(
        './template/'
)
app = Flask(__name__, template_folder=templates_path)


@app.before_request
def before_request_func():
    MySQLdb()  # create database


@app.after_request
def after_request_func(response):
    MySQLdb.close()
    return response


@app.route('/case01', methods=['GET', 'POST'])
def tbl_post01():
    if request.method == 'GET':
        return render_template("case01.html")
    user = request.form.get('user')
    model = TblPost01()
    valid, rows = model.unsafe_select_query(user)
    # valid, result = get_results_case01(query)
    if valid:
        return render_template("case01.html", results=rows)
    return render_template("case01.html", error=rows)


@app.route('/case02', methods=['GET', 'POST'])
def tbl_post02():
    if request.method == 'GET':
        return render_template("case02.html")
    comment = request.form.get('comment')
    model = TblPost02()
    # set default values
    pin = 0
    age = 0
    user = 'anonymous'
    valid, rows = model.unsafe_insert_query(comment, pin, age, user)
    if valid:
        valid, rows = model.safe_select_query()
        if valid is True:
            return render_template("case02.html", results=rows)
        else:
            return render_template("case02.html", error=rows)
    return render_template("case02.html", error=rows)


@app.route('/case03', methods=['GET', 'POST'])
def tbl_post03():
    if request.method == 'GET':
        return render_template("case03.html")
    comment = request.form.get('comment')
    model = TblPost03()
    # set default values
    city = 'san jose'
    age = 0
    random_string = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(10))
    user = 'anonymous' + '-' + random_string
    valid, rows = model.unsafe_insert_query(comment, city, age, user)
    if valid:
        valid, rows = model.safe_select_query()
        if valid is True:
            return render_template("case03.html", results=rows)
        else:
            return render_template("case03.html", error=rows)
    return render_template("case03.html", error=rows)


if __name__ == '__main__':
    app.run(debug=True)
