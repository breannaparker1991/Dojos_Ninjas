from flask_app import app 
from flask import Flask, redirect, request, render_template
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
  all = Dojo.all()
  return render_template("index.html", dojos = all)

@app.route('/new/dojo', methods=["POST"])
def new_dojo():
  data = {
    "name": request.form["name"]
  }
  Dojo.create(data)
  return redirect('/')


@app.route('/show/dojo/<int:id>')
def show(id):
  data = {
    'id' : id
  }
  return render_template("show.html", dojo = Dojo.one(data))