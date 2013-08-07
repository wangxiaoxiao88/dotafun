#-*- coding:utf-8 -*-

from flask import Flask,session,g
import config
import MySQLdb
import MySQLdb.cursors

app = Flask(__name__)
app.config.update(
	SECRET_KEY = config.SECRET_KEY,
	SESSION_COOKIE_NAME = config.SESSION_COOKIE_NAME,
	PERMANENT_SESSION_LIFETIME = config.PERMANENT_SESSION_LIFETIME)


#before every request
@app.before_request
def before_request():
    g.user_id = session['user_id'] if 'user_id' in session else None
    g.conn = MySQLdb.connect(host=config.DB_HOST, user=config.DB_USER, passwd=config.DB_PASSWD, db=config.DB_NAME, use_unicode=True, charset='utf8', cursorclass=MySQLdb.cursors.DictCursor)
    g.cursor = g.conn.cursor()
    
# after every request
@app.teardown_request
def teardown_request(exception):
    g.conn.close()
    
import log
import controllers
    
    