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

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    # Dummy check for username and password (use database in production)
    if auth.username == 'admin' and auth.password == 'admin123':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
                           app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

@app.route("/customers/search", methods=["GET"])
@token_required
def search_customers(current_user):
    customer_id = request.args.get('id')
    if customer_id is None:
        return jsonify({'message': 'Missing id parameter'}), 400
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Customers WHERE CustomerID = %s", (customer_id,))
    data = cur.fetchone()
    cur.close()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Customer not found'}), 404
    
    @app.route("/orders/search", methods=["GET"])
@token_required
def search_orders(current_user):
    order_id = request.args.get('id')
    if order_id is None:
        return jsonify({'message': 'Missing id parameter'}), 400
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Orders WHERE OrderID = %s", (order_id,))
    data = cur.fetchone()
    cur.close()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Order not found'}), 404
    
    @app.route("/menu/search", methods=["GET"])
@token_required
def search_menu(current_user):
    menu_item_id = request.args.get('id')
    if menu_item_id is None:
        return jsonify({'message': 'Missing id parameter'}), 400
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Menu WHERE MenuItemID = %s", (menu_item_id,))
    data = cur.fetchone()
    cur.close()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'message': 'Menu item not found'}), 404