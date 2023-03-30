from flask import Flask, render_template, request,jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from model import db, seedData, Customer



basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.sqlite')
db.app = app 
db.init_app(app)

@app.route("/api/customers")
def apiCustomers():
    lista = []
    for c in Customer.query.all():
        cdict = { "Id": c.Id, 
                 "Name":c.GivenName + " " + c.Surname, 
                 "City":c.City }
        lista.append(cdict)
 
    return jsonify(lista)

with app.app_context():
    db.create_all()
    seedData(app,db)
    app.run()