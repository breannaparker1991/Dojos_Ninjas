
from flask_app import app 
from flask import Flask, redirect, request, render_template
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo


@app.route('/ninja/new')
def new():
  dojos = Dojo.all()
  return render_template ("new.html", dojos = dojos)

@app.route('/ninja/create', methods=["POST"])
def ninja_create():
  Ninja.create(request.form)
  return redirect('/')


  # data = {
  #  'first_name' : request.form['first_name'],
  #  'last_name' : request.form ['last_name'],
  #  'age' : request.form['age']
  # }