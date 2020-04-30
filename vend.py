from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os
import requests
import sys; print(sys.version)
from app import Beverage
from app import beverage_schema

# For the GET
allBeverages = 'http://127.0.0.1:5000/beverage'
getAllResponse = requests.get(allBeverages)

# For the GET for a specific bev
thatOneBeverage = 'http://127.0.0.1:5000/beverage/<id>'
getOneResponse = requests.get(thatOneBeverage)

# sql = requests.get(Beverage.id)

print ("")
print ("O==============================================================================O")
print ("|                             ++ Vending Machine ++                            |")
print ("|                                  Let's Vend                                  |")
print ("O==============================================================================O")
print ("")

def vendingMachine():
    vend = ""
    spec = ""
    while vend != "a" and vend != "b" and vend != "c" and vend != "d" and vend != "e":
        print("Welcome to your local vending machine. What the heck do ya wanna do today?")
        print("")
        print("a) Check All Inventory")
        print("b) Check Certain Inventory")
        print("c) Make A Purchase")
        print("d) Add Drinks")
        print("e) Buzz Off")
        print("")
        vend = input("Make a selection: ").lower().strip()

    if vend == "a":
        print("")
        print("")
        print("Wanna check the inventory, huh?")
        print("Well, here ya go...")
        print("")
        print(getAllResponse.text)
        print("")
        print("Happy now?")
        print("")
        vendingMachine()

    if vend == "b":
        print("")
        print("")
        print("Wanna check a specific inventory item?")
        spec = input("Enter specific id: ").lower().strip()
        oneBeverage = Beverage.query.get(id)
        print(beverage_schema.jsonify(oneBeverage))
        print("")
        print("")
        vendingMachine()
    
    if vend == "c":
        print("")
        print("")
        print("Wanna make a purchase?")
        print("Try again later.")
        print("")
        print("")
        exit()
    
    if vend == "d":
        print("")
        print("")
        print("Wanna load up the inventory?")
        print("Try again later.")
        print("")
        print("")
        exit()

    if vend == "e":
        print("")
        print("")
        print("Buzz off, huh?")
        print("Get outta here.")
        print("")
        print("")
        exit()

vendingMachine()