from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os
import requests
import sys; print(sys.version)

# For the GET
allBeverages = 'http://127.0.0.1:5000/beverage'
getAllResponse = requests.get(allBeverages)

# For the GET for a specific bev
thatOneBeverage = 'http://127.0.0.1:5000/beverage/<id>'
getOneResponse = requests.get(thatOneBeverage)

# sql = 

print ("")
print ("O==============================================================================O")
print ("|                             ++ Vending Machine ++                            |")
print ("|                                  Let's Vend                                  |")
print ("O==============================================================================O")
print ("")

# def specificId():
#     spec = ""
#     while 

def vendingMachine():
    vend = ""
    query = ""
    while vend != "a" and vend != "b" and vend != "c" and vend != "d" and vend != "e":
        print("Welcome to your local vending machine. What the heck do ya wanna do today?")
        print("a) Check All Inventory")
        print("b) Check Certain Inventory")
        print("c) Make A Purchase")
        print("d) Add Drinks")
        print("e) Buzz Off")
        vend = input("Make a selection: ").lower().strip()

    if vend == "a":
        print("")
        print("")
        print("Wanna check the inventory, huh?")
        print("Well, here ya go...")
        print("")
        print(getAllResponse.text)
        print("")
        print("Happy now? Now what?")
        print("")
        vendingMachine()

    if vend == "b":
        print("")
        print("")
        print("Wanna check a specific inventory item?")
        query = input("Enter specific id: ").lower().strip()
        print("")
        print("")
        vendingMachine()
    
    if vend == "c":
        print("")
        print("")
        print("Wanna make a purchase?")
        print("Ok fine.")
        print("")
        print("")
        vendingMachine()
    
    if vend == "d":
        print("")
        print("")
        print("Wanna load up the inventory?")
        print("Sure, pal.")
        print("")
        print("")
        vendingMachine()

    if vend == "e":
        print("")
        print("")
        print("Buzz off, huh?")
        print("Get outta here.")
        print("")
        print("")
        exit()

vendingMachine()