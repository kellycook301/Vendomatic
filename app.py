from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from beverage import Beverage, beverage_schema, beverages_schema
from beverage import BeverageSchema
import os
import requests
import sys; print(sys.version)

# Creating a vending machine application that the user may interact with.
# Looking to have the user interact with the data via the command line

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

# Routes
@app.route('/beverage', methods=['POST'])
def add_beverage():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    new_beverage = Beverage(name, description, price, quantity)

    db.session.add(new_beverage)
    db.session.commit()

    return beverage_schema.jsonify(new_beverage)

@app.route('/beverage', methods=['GET'])
def get_beverages():
    all_beverages = Beverage.query.all()
    result = beverages_schema.dump(all_beverages)
    return jsonify(result)

@app.route('/beverage/<id>', methods=['GET'])
def get_beverage(id):
    beverage = Beverage.query.get(id)
    return beverage_schema.jsonify(beverage)

@app.route('/beverage/<id>', methods=['PUT'])
def update_beverage(id):
    beverage = Beverage.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    quantity = request.json['quantity']

    beverage.name = name
    beverage.description = description
    beverage.price = price
    beverage.quantity = quantity

    db.session.commit()

    return beverage_schema.jsonify(beverage)

@app.route('/beverage/<id>', methods=['DELETE'])
def delete_beverage(id):
    beverage = Beverage.query.get(id)
    db.session.delete(beverage)
    db.session.commit()
    return beverage_schema.jsonify(beverage)

# Let's start this sucker...

# Run the freaking server
if __name__ == '__main__':
    app.run(debug=True)