# Automation Team - Technical Challenge

---

# What is this?

This is my take on a very simple store project. You can add products to the store's inventory, you can see what's in it, you can delete some unwanted items and more.


---

# Instructions on how to build

I managed to dockerize this application so you (hopefully) won't have to run it locally.

```docker-compose up -d --build```  To build this application's image


(if for some reason the migrations didn't go through: ```docker-compose run web python3 manage.py migrate``` )

## Where do I test the routes? 

``` 0.0.0.0:8080 ``` was my choice for testing the application.


## What routes do we get?

I tried using a plugin to generate a doc automatically from insomnia but failed (see here https://mmdsza.github.io/insomnia.json)

### /api/lojinha

GET: shows all products available, (name, price, size and a description. Supports query params. e.g. /api/lojinha?name=calca will return all products with "calca" in their names.

POST: Adds a new product! Takes {Name:name, price:price, description:description, size:size) on Body. Sizes range from "S, M, L".

DELETE: if no id provided (/api/lojinha/1, for example) will delete ALL products on the database.

PUT: Given a product id (/api/lojinha/1) and a body with new product information, it will update the product's info on the database.







