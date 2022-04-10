from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
  db = "Dojos_Ninjas"
  def __init__(self, data):
    self.id = data['id']
    self.first_name = data['first_name']
    self.last_name = data['last_name']
    self.age = data['age']
    self.created_at = data['created_at']
    self.updated_at = data['updated_at']
    
  @classmethod
  def create(cls, data):
    query = "INSERT INTO ninja (first_name, last_name, age, dojo_id)  VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s )"
    result = connectToMySQL(cls.db).query_db(query, data)
    return result
  
  
