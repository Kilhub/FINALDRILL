from flask import Flask, make_response, jsonify, request
from flask_mysqldb import MySQL
import jwt
import datetime
from functools import wraps

app = Flask(__name__)

# MySQL configuration
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "mysql"
app.config["MYSQL_DB"] = "RestaurantDB"
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

app.config['SECRET_KEY'] = 'admin123'


def data_fetch(query, params=None):
    cur = mysql.connection.cursor()
    cur.execute(query, params)
    data = cur.fetchall()
    cur.close()
    return data

from functools import wraps
from flask import request, jsonify

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = data['user']
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)
    return decorated