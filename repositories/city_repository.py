from unittest import result
from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository

#CRUD
#CREATE
def save(city):
    sql = """
        INSERT INTO cities (name, visit, country_id)
        VALUES (%s, %s, %s)
        RETURNING *
    """
    values = [city.name, city.visit, city.country.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

#READ
def select_all():
    cities = []
    sql = "SELECT * FROM  cities"
    
    results = run_sql(sql)

    for row in results:
        #create obj and push into list(orders matter)
        country = country_repository.select(row['country_id'])
        city = City(row['name'], country, row['visit'], row['id'])
        cities.append(city)
    return cities    



def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        country = country_repository.select(result['country_id'])
        city = City(result['name'], country, result['visit'], result['id'] )
    return city

#UPDATE
def update(city):
    sql = """
        UPDATE cities
        SET (name,country_id, visit, id ) =  (%s, %s, %s, %s)
        WHERE id = %s
    """
    values = [city.name, city.country.id, city.visit, city.id]
    run_sql(sql, values)

#DELETE
def delete_all():
    sql = """
        DELETE FROM cities
    """
    run_sql(sql)

def delete(id):
    sql = """
        DELETE FROM cities
        WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)
  

    





