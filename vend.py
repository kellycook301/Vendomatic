from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
import requests
import simplejson as json
import getpass
from app import Beverage
from app import beverage_schema
import sys; print(sys.version)
import os

def addBeverage():
    beverageEndpoint = 'http://127.0.0.1:5000/beverage'
    header = {"content-type": "application/json"}
    beveragePost = {}
    beveragePost["name"] = input("Enter a name: ").strip()
    beveragePost["description"] = input('Enter item description: ').strip()
    beveragePost["price"] = input("Enter price of item (no need to add '$'): ").strip()
    beveragePost["quantity"] = input("Enter how many items you are adding: ").strip()
    print("")
    print(beveragePost)
    print("")
    answer = input("Does this look good to you? y/n \n").lower().strip()
    if answer == "y":
        print("")
        print(requests.post(beverageEndpoint, data=json.dumps(beveragePost), headers=header, verify=False).text)
    
    elif answer == "n":
        print("")
        print("No problem, bud.")
        print("")
        vendingMachine()

    else:
        print("Try typing something that I actually understand, dummy.")
        print("")
        addBeverage()

def purchaseOneBeverage():
    beverageEndpoint = 'http://127.0.0.1:5000/beverage/'
    userInput = input("Enter specific id: ").strip()
    url = (beverageEndpoint + userInput)
    data = json.loads(requests.get(beverageEndpoint + userInput).text)
    quantity = (data['quantity'] - 1)
    header = {"content-type": "application/json"}
    print(requests.put(url, json=data, headers=header).text)
    print(quantity)
    print("STILL WORKING ON THIS")

def getAllBeverages():
    allBeverages = 'http://127.0.0.1:5000/beverage'
    getAllBeveragesResponse = requests.get(allBeverages)
    print("")
    print(getAllBeveragesResponse.text)

def getOneBeverage():
    singleBeverage = 'http://127.0.0.1:5000/beverage/'
    getOneResponse = requests.get(singleBeverage)
    userInput = input("Enter specific id: ").strip()
    print("")
    print(requests.get(singleBeverage + userInput).text)

def deleteOneBeverage():
    singleBeverage = 'http://127.0.0.1:5000/beverage/'
    deleteOneResponse = requests.delete(singleBeverage)
    userInput = input("Enter specific id: ").strip()
    print("")
    print(requests.get(singleBeverage + userInput).text)
    answer = input("Is this the beverage you are looking to delete? y/n \n").lower().strip()
    if answer == "y":
        print("")
        print(requests.delete(singleBeverage + userInput).text)

    elif answer == "n":
        print("")
        print("No problem, bud.")
        print("")
        vendingMachine()

    else:
        print("Try typing something that I actually understand, dummy.")
        print("")
        deleteOneBeverage()

print ("")
print ("O==============================================================================O")
print ("|                             ++ Vending Machine ++                            |")
print ("|                                  Let's Vend                                  |")
print ("O==============================================================================O")
print ("")

def vendingMachine():
    vend = ""
    userInput = ""
    print("Welcome to your local vending machine. What the heck do ya wanna do today?")
    print("")
    print("a) Check All Inventory")
    print("b) Check Certain Inventory Item")
    print("c) Make A Purchase")
    print("d) Add Beverage")
    print("e) Get Rid Of A Beverage")
    print("f) Exit Vending Machine")
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

    elif vend == "b":
        print("")
        print("Wanna check a specific inventory item?")
        getOneBeverage()
        print("Happy now?")
        print("")
        vendingMachine()
    
    elif vend == "c":
        print("")
        print("Wanna make a purchase?")
        purchaseOneBeverage()
        print("")
        exit()
    
    elif vend == "d":
        print("")
        print("Wanna load up the inventory? You must be a vending machine operator.")
        print("Go ahead and enter the super secret password.")
        vending_machine_password = getpass.getpass('Password:')
        if vending_machine_password == "password":
            addBeverage()
            print("Beverage/s added!")
            print("")
            vendingMachine()
        else:
            print("")
            print("Try again, bud.")
            print("")
            vendingMachine()

    elif vend == "e":
        print("")
        print("")
        print("Wanna get rid of certain items?")
        print("Go ahead and enter the super secret password.")
        vending_machine_password = getpass.getpass('Password:')
        if vending_machine_password == "password":
            deleteOneBeverage()
            print("Beverage/s deleted!")
            print("")
            vendingMachine()
        else:
            print("")
            print("Try again, bud.")
            print("")
            vendingMachine()

    elif vend == "f":
        print("")
        print("")
        print("See ya later, bud.")
        print("")
        print("")
        exit()

    else:
        print("")
        print("")
        print("Try typing something that I actually understand, dummy.")
        print("")
        print("")
        vendingMachine()

vendingMachine()