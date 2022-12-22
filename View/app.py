import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_clc_by_depositId(deposit_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM CAO_Data WHERE deposit_id = ?',
                        (deposit_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_clc_by_jcNum(jc_num):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM CAO_Data jc_number id = ?',
                        (jc_num,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_clc_by_jcName(jc_name):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM CAO_Data WHERE jc_name = ?',
                        (jc_name,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_clc_by_them(theme):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM CAO_Data WHERE nl_theme = ?',
                        (theme,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_clc_by_retrieveDate(retrieve_date):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM CAO_Data WHERE Retrieve_Date = ?',
                        (retrieve_date,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

def get_clc_by_depositDate(deposit_date):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM CAO_Data WHERE Deposite_Date = ?',
                        (deposit_date,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    # posts = conn.execute('SELECT * FROM CAO_Data').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    # app.debug = True
    app.run()
