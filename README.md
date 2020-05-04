
# Let's Get Vendy: The Vending Machine With ATTITUDE

With this app you may check beverage inventory, add more beverages, get rid of unwanted beverages, and purchase beverages (...eventually). This is semi-inspired by a 'choose your own adventure' game that I was working on as well as the Guitar Center point-of-sale system.
Created a REST API with Flask, SQLAlchemy, and Marshmallow.

Let's get started!

## Launching The App

Let's get the app set up first.

1. Clone the git repository
```
git clone git@github.com:kellycook301/pythonCLItest.git
```

2. Install pip if you don't have that.
```
install pip
```

3. Install pipenv if you don't have that either
```
install pipenv
```

1. You are also gonna need Flask, SQLAlchemy, and Marshmallow.
```
install Flask/SQLAlchemy/Marshmallow
```

5. Run pipenv shell
```
pipenv shell
```

6. cd to the appropriate directory

7. Run the server from the project directory
```
python app.py
```

8. Open up a new tab and enter the pipenv shell again. Then naviagate to the directory and start the vending machine
```
pipenv shell
```

```
python vend.py
```

## Testing The App

1. You can start testing the application cnce the app is running

### Getting All Beverages

2. Entering a) for "Check All Inventory" will return all beverages. Simple stuff, ya know?

### Getting A Specific Beverage

3. Entering b) for "Check Certain Inventory Item" will prompt you for an id. Enter the id to return the corresponding beverage.

### Making A Purchase

4. This is actually something I am still working on! The idea will be that you will enter a certain id and doing so will reduce the quantity of said item by 1. When the quantity of any item is 0 then it will be deleted. Still working on this!

### Adding A New Beverage

5. Entering d) for "Add Beverage" will first prompt you for a password. We can't just have any ol' person adding inventory items to the vending machine, so go ahead and input the password "password." Super secret stuff. You will then be prompted for a name, description, price, and quantity for said item/s. Then you'll be asked if everything looks good to you before finally submitting. Upon completion, you will see the result printed to the screen.

### Deleting An Existing Beverage

6. Entering e) for "Get Rid Of A Beverage" will once again prompt you for the super secret password. you will then be prompted to input the id of a beverage. After confirming that this is the beverage you want gone, it will be deleted.

