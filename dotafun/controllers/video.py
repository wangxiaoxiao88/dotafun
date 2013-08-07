#-*- coding: utf-8 -*-

from flask import render_template, request, url_for
from dotafun import app

@app.route('/index')
def index():
    return 'dotafun index'