# AskNRA API Proof of Concept
* */* : this route doesn't need credentials.
* */login* : client sends username and password in plain text in JSON format ({username:'name',password:'pass'}) (POST). If login is correct, the client receives the JWT token.
* */unprotected* : this route doesn't need credentials.
* */nra-only*: Only logged user with "nra" rol can acces. Checks the request header named "Authorization" which contains the JWT token obtained after succes login.
* */onlyusers*: Similar to previous route. Only "user" rol is accepted.

## How to use
1. Clone or download this repository
2. Install the dependencies:
```
$ pip install -r requirements.txt
```
3. Run the server using run.py file:
```
$ python run.py
```
4. The server should be accesible on http://localhost:5000/ 
5. The file **app/db.py** contains info in a dictionary. It is used like a database.
6. Open the **/jwt_collection** folder in [Bruno API Client](https://www.usebruno.com/) to start testing the API.