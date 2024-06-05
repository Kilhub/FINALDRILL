Restaurant Management API
Introduction
This Flask-based RESTful API is designed to manage various aspects of a restaurant, including customer information, orders, menu items, and payments. It provides functionalities such as user authentication using JSON Web Tokens (JWT) and supports CRUD (Create, Read, Update, Delete) operations for different entities within the restaurant.

Features
Authentication: Utilizes JWT for user authentication, ensuring secure access to API endpoints.
CRUD Operations: Supports fundamental CRUD operations for customers, orders, menu items, and payments, enabling efficient management of restaurant data.
Search Functionality: Provides search functionality for customers, orders, menu items, and payments based on specific criteria.
Data Retrieval: Retrieves data for customers, orders, menu items, and payments, facilitating easy access to relevant information.
MySQL Integration: Integrates with MySQL database for storing and managing restaurant data efficiently.
Prerequisites
To set up and run the API, ensure the following prerequisites are met:

Python 3.x
Flask
Flask-MySQLDB
PyJWT

Installation
1. Clone the repository:
   git clone <repository_url>

2. Install the required dependencies:
   pip install Flask Flask-MySQLDB PyJWT

3. Set up MySQL database:
   Create a database named RestaurantDB.
  Set your MySQL username and password in api.py

  app.config["MYSQL_USER"] = "root"
  app.config["MYSQL_PASSWORD"] = "your_password_here"

4. Run the Flask application:
python api.py

API Endpoints
Authentication
POST /login: Authenticates users and generates JWT token.
Customers
GET /customers: Retrieves all customers.
GET /customers/<int:id>: Retrieves a customer by ID.
POST /customers: Adds a new customer.
PUT /customers/<int:id>: Updates an existing customer.
Orders
GET /orders: Retrieves all orders.
GET /orders/<int:id>: Retrieves an order by ID.
Menu
GET /menu: Retrieves all menu items.
GET /menu/<int:id>: Retrieves a menu item by ID.
Payments
GET /payments: Retrieves all payments.
GET /payments/<int:id>: Retrieves a payment by ID.
Search
GET /customers/search: Searches for customers based on provided criteria.
GET /orders/search: Searches for orders based on provided criteria.
GET /menu/search: Searches for menu items based on provided criteria.
GET /payments/search: Searches for payments based on provided criteria.
GET /employees/search: Searches for employees based on provided criteria.
Additional Operations
GET /customers/<int:id>/orders: Retrieves orders associated with a specific customer.
DELETE /employees/<int:id>: Deletes an employee by ID.

Testing
Before running unit tests, ensure dependencies are installed and the API is running. Execute the tests:
python test.py

Additional Notes
Properly configure MySQL settings and implement security measures before deploying the API in production environments.
Ensure to provide adequate error handling and input validation mechanisms to enhance the robustness and reliability of the API.


