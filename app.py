from flask import Flask, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Creating a vending machine application that the user may interact with.
# Looking to have the user interact with the data via the command line

# Init App
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)

#Init Marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Beverage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

# Product Schema
class BeverageSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'quantity')

# Init Schema
beverage_schema = BeverageSchema()
beverages_schema = BeverageSchema(many=True)

# Create a Beverage
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

# Routes
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

# Run server
if __name__ == '__main__':
    app.run(debug=True)