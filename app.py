from enum import unique
from flask import Flask,request,jsonify

from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

import datetime

import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#DB

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db = SQLAlchemy(app)

ma = Marshmallow(app)

#Product ---> UserData

class Product(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    First_Name = db.Column(db.String(100))
    Last_Name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    Education = db.Column(db.String(100))
    City = db.Column(db.String(100))
    email = db.Column(db.String(100))
    create_at = db.Column(db.String(100))

    def __init__(self,First_Name,Last_Name,age,Education,City,email,create_at):

        self.First_Name = First_Name
        self.Last_Name = Last_Name
        self.age = age
        self.Education = Education
        self.City = City
        self.email = email
        self.create_at = create_at
        

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id','First_Name','Last_Name','age','Education','City','email','create_at')


product_schema = ProductSchema()
products_schema = ProductSchema(many = True)

#creating the routes

@app.route('/')
def get():
    return ("Welcome move to /product")

@app.route('/product',methods = ['POST'])
def add_product():
    First_Name = request.json['First_Name']
    Last_Name = request.json['Last_Name']
    age = request.json['age']
    Education = request.json['Education']
    City = request.json['City']
    email = request.json['email']
    create_at = request.json['create_at']

    new_product = Product(First_Name,Last_Name,age,Education,City,email,create_at)

    db.session.add(new_product)

    db.session.commit()


    return product_schema.jsonify(new_product)



@app.route('/product',methods = ['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)



if __name__ == '__main__':
    app.run(debug=True)
