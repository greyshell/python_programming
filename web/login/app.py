#!/usr/bin/env python3

# author: greyshell

import os

from flask import Flask, render_template, session, redirect, url_for, jsonify
from flask import request
from web.login.models import *

templates_path = os.path.abspath(
        './template/'
)
app = Flask(__name__, template_folder=templates_path)
app.config.update(dict(
        SECRET_KEY="woopie"
))


def get_logged_in_user():
    if "userid" not in session:
        return None
    return User.logged_user(session['userid'])


@app.before_request
def before_request_func():
    MySQLdb()  # create database


@app.after_request
def after_request_func(response):
    MySQLdb.close()
    return response


@app.route('/', methods=['GET', 'POST'])
def index():
    user = get_logged_in_user()
    if user is not None:
        return redirect(url_for('welcome'))
    if request.method == 'GET':
        return render_template("index.html")
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.get_user(username, password)
    if not user:
        return render_template("index.html", error="User not found")
    session['userid'] = user.id
    return redirect(url_for('welcome'))


@app.route('/welcome', methods=['GET'])
def welcome():
    user = get_logged_in_user()
    if user is None:
        return redirect(url_for("index"))
    return render_template('welcome.html', user=user)


@app.route('/update_age', methods=['POST'])
def update_age():
    user = get_logged_in_user()
    if user is None:
        return jsonify(status="User not logged in")
    print(request.get_json())
    age = int(request.json['age'])
    user.age = age
    success = user.save()
    if success[0]:
        return jsonify(status="Age successfully changed")
    else:
        return jsonify(status="error " + success[1])


@app.route('/logout')
def logout():
    if 'userid' in session:
        session['userid'] = None
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)
