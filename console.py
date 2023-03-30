from flask import Flask
import os
from model import db, seedData, Customer
from game import gissaEttTal 
from customerservice import customerservice_searchOnCity

def customerCityList():
    citystart = input("Ange början på städer (ex st ) att leta efter")
    for x in customerservice_searchOnCity(citystart):
        print(f"{x.GivenName} {x.Surname}")

def menu():
    while True:
        print("1. Lista alla kunder som bor i city")
        print("2. Lista alla kunder med långa namn")
        print("3. Verifiera usernames")
        print("4. Gissa ett tal")
        print("9. Avsluta ")
        selection = int(input("Ange val:"))
        if selection == 1:
            customerCityList()
        if selection == 4:
            gissaEttTal()
        if selection == 9:
            return


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.sqlite')
db.app = app 
db.init_app(app)


with app.app_context():
    db.create_all()
    menu()
