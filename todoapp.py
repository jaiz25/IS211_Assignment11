#!usr/bin/env/python
# -*- coding: utf-8 -*-
"""Assignment 11 for IS211"""


from flask import Flask, render_template, request, redirect
import re
app = Flask(__name__)
task_list = []


@app.route('/')
def to_do_list():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    task = request.form['task']
    email = request.form['email']
    if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
        return redirect('/')
    priority = request.form['priority']
    if priority == 'none':
        return redirect('/')
    else:
        task_list.append(task)
        return render_template('index.html', task_list=task_list)


@app.route('/clear', methods=['POST'])
def clear():
    clear = request.form['clear']
    return redirect('/')


if __name__ == '__main__':
    app.run()
