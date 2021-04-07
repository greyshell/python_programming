#!/usr/bin/env python3

# author: greyshell

import os
import random
import string
from flask import Flask, render_template
from flask import request
from models import *
from mysql_db import MySQLdb

templates_path = os.path.abspath(
        './template/'
)
app = Flask(__name__, template_folder=templates_path)


@app.before_request
def before_request_func():
    # create the database
    MySQLdb(host="localhost", db_name="vulnapp")


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
    return_type, rows = model.unsafe_select_query(user)
    if return_type:
        return render_template("case01.html", results=rows)
    return render_template("case01.html", error=rows)


@app.route('/case02', methods=['GET', 'POST'])
def tbl_post02():
    if request.method == 'GET':
        return render_template("case02.html")
    comment = request.form.get('comment')
    model = TblPost02()

    pin = 0  # set default value
    age = 0  # set default value
    user = 'anonymous'  # set default value
    return_type, rows = model.unsafe_insert_query(comment, pin, age, user)
    if return_type:
        return_type, rows = model.safe_select_query()
        if return_type:
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
    # check if the user already exists
    return_type, rows = model.is_exist_user(user)
    if return_type:
        return render_template("case03.html", error='user already exists / had exception')

    return_type, rows = model.unsafe_insert_query(comment, city, age, user)
    if return_type:
        return_type, rows = model.safe_select_query()
        if return_type:
            return render_template("case03.html", results=rows)
        else:
            return render_template("case03.html", error=rows)
    return render_template("case03.html", error=rows)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
