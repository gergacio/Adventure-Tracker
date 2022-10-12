
from db.run_sql import run_sql
from models.country import Country
from models.city import City
#repository is a middleware between database and models(import models)
#CRUD - do all crud (use them in the future)
#CREATE - give sql string to run_sql method to do all job for us
#get back list of dictinary like objs and get value by given key(id in our case)
def save(country):
    sql = """
        INSERT INTO countries (name, description, visit) 
        VALUES (%s, %s, %s)
        RETURNING *
    """
    values = [country.name,country.description, country.visit]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

#Read - Select from countries table ..loop (results = list of dicts) 
def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    values = []
    results = run_sql(sql, values)

    for row in results:
        #create obj and push into list(orders matter)
        country = Country(row['name'],row['description'], row['visit'], row['id'])
        countries.append(country)
    return countries    

def select(id):
    country = None
    sql = """
        SELECT * FROM countries 
        WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        #just one result by id
        result = results[0]
        country = Country(result['name'], result['description'], result['visit'], result['id'])

    return country   

#UPDATE
def update(country):
    sql = "UPDATE countries SET (name, description, visit) = (%s, %s, %s) WHERE id = %s"
    values = [country.name, country.description, country.visit, country.id]
    run_sql(sql, values)

#DELETE
def delete_all():
    sql = """
        DELETE FROM countries
    """
    run_sql(sql)

def delete(id):
    sql = """
        DELETE FROM countries
        WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

#cities by country
  
  
 
    




