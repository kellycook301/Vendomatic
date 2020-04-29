import os
import requests
import sys; print(sys.version)

url = 'http://127.0.0.1:5000/beverage'
response = requests.get(url) 

print ("")
print ("O==============================================================================O")
print ("|                             ++ Vending Machine ++                            |")
print ("|                                  Let's Vend                                  |")
print ("O==============================================================================O")
print ("")

def vendingMachine():
    vend = ""
    while vend != "a" and vend != "b" and vend != "c" and vend != "d":
        print("Welcome to your local vending machine. What the heck do ya wanna do today?")
        print("a) Check Inventory")
        print("b) Make A Purchase")
        print("c) Add Drinks")
        print("d) Buzz Off")
        vend = raw_input("Make a selection / \n").lower().strip()

    if vend == "a":
        print("")
        print("")
        print("Wanna check the inventory, huh?")
        print("Well, here ya go...")
        print(response.text)
        print("")
        print("")
        vendingMachine()
    
    if vend == "b":
        print("")
        print("")
        print("Wanna make a purchase?")
        print("Ok fine.")
        print("")
        print("")
        vendingMachine()
    
    if vend == "c":
        print("")
        print("")
        print("Wanna load up the inventory?")
        print("Sure, pal.")
        print("")
        print("")
        vendingMachine()

    if vend == "d":
        print("")
        print("")
        print("Wanna buzz off?")
        print("Get outta here.")
        print("")
        print("")
        exit()

vendingMachine()