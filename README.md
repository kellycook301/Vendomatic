
# Let's Get Vendy: The Vending Machine With ATTITUDE

With this app you may check beverage inventory, add more beverages (eventually), updated inventory (...eventually), and get rid of unwanted beverages (...also eventually). This is semi-inspired by a 'choose your own adventure' game that I was working on...and the crappy Guitar Center POS system (long live Green Screen).
Created a REST API with Flask, SQLAlchemy, and Marshmallow.
Without launching the Python shell you can do some curl commands if you wanna do requests that way. I just have GETs for now.

```
# curl -i -X GET http://127.0.0.1:5000/beverage
```
```
# curl -i -X GET http://127.0.0.1:5000/beverage/1
```
You can also check in Postman if that's your thing.

Let's get started!

## Launching The App

Let's get the app set up first.

1. Clone the git repository
```
git clone https://google.com
```

2. Install pip if you don't have that.
```
install pip
```

3. Install pipenv if you don't got it
```
install pipenv
```
4. You are also gonna need Flask, SQLAlchemy, and Marshmallow (yay dependencies!)
```
install Flask/SQLAlchemy/Marshmallow
```

5. Run the server from the project directory
```
python app.py
```

6. Open up a new tab and start the vending machine
```
python vend.py
```

7. Test functionality by performing various requests. Checking all inventory will get back all beverages. For getting a specific beverage, enter an id and see what comes back. If the id doesn't exist, you'll get "{}" as a response. Don't take it personally.

8. Obviously, I gotta add some error handling. Gimme some time, k?

