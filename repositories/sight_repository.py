

from db.run_sql import run_sql
from models.city import City
from models.sight import Sight
import repositories.city_repository as city_repository

#CRUD
#create - use insert into 
def save(sight):
    sql = """
        INSERT INTO sights (name, visit, city_id)
        VALUES (%s, %s, %s)
        RETURNING *
    """
    values = [sight.name, sight.visit, sight.city.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    sight.id = id
    return sight
    


#read
def select_all():
    sights = []
    sql = "SELECT * FROM sights"
    results = run_sql(sql)

    for row in results:
        #create obj and push into list(orders matter)
        city = city_repository.select(row['city_id'])
        sight = City(row['name'], city, row['visit'], row['id'])
        sights.append(sight)
    return sights   


def select(id):
    sight = None
    sql = "SELECT * FROM sights WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        city = city_repository.select(result['city_id'])
        sight = Sight(result['name'], city, result['visit'], result['id'] )
    return sight

#update
def update(sight):
    sql = """
    UPDATE sights
    SET (%s, %s, %s, %s)
    WHERE id = %s
    """
    values = [sight.name, sight.city.id, sight.visit, sight.id]
    run_sql(sql, values)


#delete
def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

def delete(id):
    sql = """
        DELETE FROM sights 
        WHERE id = %s
    """
    values = [id]

    run_sql(sql, values)

