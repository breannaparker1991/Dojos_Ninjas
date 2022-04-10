from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
  db = "Dojos_Ninjas"
  def __init__(self,data):
    self.id = data['id']
    self.name = data['name']
    self.created_at = data['created_at']
    self.ninjas = []
    
  @classmethod
  def create(cls, data):
    query = "INSERT INTO dojo (name, created_at)  VALUES ( %(name)s, NOW() )"
    result = connectToMySQL(cls.db).query_db(query, data)
    return result
  
  @classmethod
  def all(cls):
    query = "SELECT * FROM dojo"
    result = connectToMySQL(cls.db).query_db(query)
    print(result)
    dojos = []
    for d in result:
      dojos.append(cls(d))
    return dojos
  
  @classmethod
  def one(cls, data):
    query = "SELECT * FROM dojo LEFT JOIN ninja on ninja.dojo_id = dojo.id WHERE dojo.id = %(id)s"
    results = connectToMySQL(cls.db).query_db(query,data)
    NinDoj = cls(results[0]) 
    for d in results:
      data = {
        'id' : d['ninja.id'],
        'first_name' : d['first_name'],
        'last_name' : d['last_name'],
        'age' : d['age'], 
        'created_at': d['ninja.created_at'], 
        'updated_at': d['ninja.updated_at']
      }
      NinDoj.ninjas.append( Ninja(data))
    return  NinDoj
  