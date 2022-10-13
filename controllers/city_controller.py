
from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository


city_blueprint = Blueprint("cities", __name__)

#routes
#list sities by country index
#cities routes

@city_blueprint.route('/cities/<id>', methods = ["GET"])
def cities_by_country_id(id):
    country = country_repository.select(id)
    cities = city_repository.select_all()
    r_cities = []
    for city in cities:
        if city.country.id == int(id):
            r_cities.append(city)
    
    return render_template('/cities/index.html', country = country, cities = r_cities)

@city_blueprint.route('/cities/new', methods = ["GET"])
def create_city_by_country():
    countries = country_repository.select_all()

    return render_template('/cities/new.html',countries = countries)   

@city_blueprint.route('/cities/create', methods = ["POST"])
def create_new_city_by_country():
    #create city
    name = request.form['city']
    visit = True if "visit" in request.form else False
    country_id = request.form['country_id']

    country = country_repository.select(country_id)

    city = City(name, country, visit)
    city_repository.save(city)
    
    
    return redirect('/countries')

  
        
@city_blueprint.route('/cities/<id>/delete', methods = ["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect ('/countries')

@city_blueprint.route('/cities/visited', methods = ["GET"])
def visited():
     visited = []
     cities = city_repository.select_all()
     for city in cities:
        if city.visit == True:
            visited.append(city)
            
     return render_template('/cities/visited.html',cities = visited)   

@city_blueprint.route('/cities/still_to_visit', methods = ["GET"])
def still_to_visit():
     still_visit = []
     cities = city_repository.select_all()
     for city in cities:
        if city.visit == False:
            still_visit.append(city)

     return render_template('/cities/still_to_visit.html',cities = still_visit)   

#search
@city_blueprint.route('/searchc', methods=["GET"])
def search_country():
    found_city = None
    name = request.args["city"]
    cities = city_repository.select_all()
    for city in cities:
        if city.name.lower() == name.lower():
            found_city = city
    return render_template('/cities/city.html', city = found_city)   








