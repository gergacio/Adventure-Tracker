from crypt import methods
from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.sight import Sight
import repositories.sight_repository as sight_repository
import repositories.city_repository as city_repository

sight_blueprint = Blueprint("sights", __name__)

#REST

#GET request
@sight_blueprint.route('/sights/<id>', methods = ["GET"])
def sights_by_city_id(id):
    city = city_repository.select(id) 
    sights = sight_repository.select_all()
    #try filter sights by given city --- can't do it

    return render_template('/sights/index.html', city = city, sights = sights)


#POST request - to put something on the server

@sight_blueprint.route('/sights/new', methods = ['GET'])    
def create_new_sight_by_city():
    cities = city_repository.select_all()
    return render_template('/sights/new.html', cities = cities)
    
@sight_blueprint.route('/sights/create', methods = ['POST'])    
def create_sight_by_city():
     #create sight (get values from outside world - request.form)
    name = request.form['sight']
    city_id = request.form['city_id']
    visit = True if "visit" in request.form else False

    city = city_repository.select(city_id)
    sight = Sight(name, city, visit)
    
    sight_repository.save(sight)
    
    return redirect('/countries')
 

@sight_blueprint.route('/sights/<id>/delete', methods = ["POST"])
def delete_sight(id):
    sight_repository.delete(id)
    return redirect ('/countries')
    



