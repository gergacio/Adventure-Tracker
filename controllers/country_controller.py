from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository


countries_blueprint = Blueprint("countries", __name__)

#routes

#list countries
@countries_blueprint.route('/countries',methods = ["GET"])
def countries():
    countries = country_repository.select_all()
    return render_template('/countries/index.html', all_countries = countries)

#create new country
@countries_blueprint.route('/countries/new', methods = ["GET"])
def new_country():
    return render_template('/countries/new.html')

@countries_blueprint.route('/countries/create', methods = ["POST"])
def create_country():
    name = request.form['country']
    description = request.form['description']
    visit = True if "visit" in request.form else False
    country = Country(name, description, visit)
    country_repository.save(country)

    return redirect('/countries')

#edit
@countries_blueprint.route('/countries/<id>/edit', methods = ["GET"])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/countries/edit.html', country = country)
    
@countries_blueprint.route('/countries/<id>/edit', methods = ["POST"])
def edit_country_post(id):
    
    name = request.form['name']
    description = request.form['description']
    visit = True if "visit" in request.form else False
    country = Country(name, description, visit, id)
    country_repository.update(country)
   
    return redirect('/countries')
    
    

#delete 
@countries_blueprint.route('/countries/<id>/delete', methods = ["POST"])
def delete_country(id):
    city_repository.delete_all()
    country_repository.delete(id)
    return redirect ('/countries')








