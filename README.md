# AskNRA API Proof of Concept
## Let's create a conceptual REST API using JWT Authentication 
* */* : this route doesn't need credentials.
* */login* : client sends username and password in plain text in JSON format ({username:'name',password:'pass'}) (POST). If login is correct, the client receives the JWT token.
* */unsers-only* : this route doesn't need credentials.
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
5. The file **/app/db.py** contains user accounts and data in dictionaries and lists It is used like a database.
6. Open the **/jwt_collection** folder in [Bruno API Client](https://www.usebruno.com/) to start testing the API.
7. Adjust the token expiration time **JWT_EXPIRATION_TIME** parameter to your needs in the **/app/security.py** file.
8. Default installed routes:
```
flask routes --sort methods

Endpoint               Methods  Rule                   
---------------------  -------  -----------------------
static                 GET      /static/<path:filename>
netz.get_net           GET      /api/net/<int:param>   
netz.get_search_net    GET      /api/net/search-net    
netz.get_netz          GET      /api/netz              
sitez.get_site         GET      /api/site/<int:param>  
sitez.get_search_site  GET      /api/site/search-site  
sitez.get_netz         GET      /api/sitez             
index                  GET      /                      
onlyadmins             GET      /nra-only              
onlyusers              GET      /users-only            
security.login         POST     /login                 
netz.add_netz          POST     /api/netz              
sitez.add_sitez        POST     /api/sitez  
```