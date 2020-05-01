from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import os
import requests
import simplejson as json
import sys; print(sys.version)
from app import Beverage
from app import beverage_schema

print ("")
print ("O==============================================================================O")
print ("|                             ++ Vending Machine ++                            |")
print ("|                                  Let's Vend                                  |")
print ("O==============================================================================O")
print ("")

def addBeverage():
    # For adding a beverage...
    oneBeverage = 'http://127.0.0.1:5000/beverage'
    header = {"content-type": "application/json"}
    beveragePost = {}
    beveragePost["name"] = input("Enter a name: ").strip()
    beveragePost["description"] = input('Enter item description: ').strip()
    beveragePost["price"] = input("Enter price of item (no need to add '$'): ").strip()
    beveragePost["quantity"] = input("Enter how many items you are adding: ").strip()
    print("")
    print(requests.post(oneBeverage, data=json.dumps(beveragePost), headers=header, verify=False).text)

def getAllBeverages():
    # For getting all beverages...
    allBeverages = 'http://127.0.0.1:5000/beverage'
    getAllBeveragesResponse = requests.get(allBeverages)
    print("")
    print(getAllBeveragesResponse.text)

def getOneBeverage():
    # For getting one beverage...
    thatOneBeverage = 'http://127.0.0.1:5000/beverage/'
    getOneResponse = requests.get(thatOneBeverage)
    userInput = input("Enter specific id: ").strip()
    print("")
    print(requests.get(thatOneBeverage + userInput).text)

def deleteOneBeverage():
    # For deleting one beverage...
    thatOneBeverage = 'http://127.0.0.1:5000/beverage/'
    deleteOneResponse = requests.delete(thatOneBeverage)
    userInput = input("Enter specific id: ").strip()
    print("")
    print(requests.delete(thatOneBeverage + userInput).text)


def vendingMachine():
    vend = ""
    userInput = ""
    while vend != "a" and vend != "b" and vend != "c" and vend != "d" and vend != "e" and vend != "f":
        print("Welcome to your local vending machine. What the heck do ya wanna do today?")
        print("")
        print("a) Check All Inventory")
        print("b) Check Certain Inventory")
        print("c) Make A Purchase")
        print("d) Add Drinks")
        print("e) Get Rid Of A Beverage")
        print("f) Buzz Off")
        print("")
        vend = input("Make a selection: ").lower().strip()

    if vend == "a":
        print("")
        print("Wanna check the inventory, huh?")
        print("Well, here ya go...")
        getAllBeverages()
        print("Happy now?")
        print("")
        vendingMachine()

    if vend == "b":
        print("")
        print("Wanna check a specific inventory item?")
        getOneBeverage()
        print("Happy now?")
        print("")
        vendingMachine()
    
    if vend == "c":
        print("")
        print("Wanna make a purchase?")
        print("Try again later.")
        print("")
        print("")
        exit()
    
    if vend == "d":
        print("")
        print("Wanna load up the inventory? You got it, bud.")
        addBeverage()
        print("Beverage added!")
        print("")
        vendingMachine()

    if vend == "e":
        print("")
        print("")
        print("Wanna get rid of certain items?")
        deleteOneBeverage()
        print("Beverage deleted!")
        print("")
        vendingMachine()

    if vend == "f":
        print("")
        print("")
        print("Buzz off, huh?")
        print("Get outta here.")
        print("")
        print("")
        exit()

vendingMachine()