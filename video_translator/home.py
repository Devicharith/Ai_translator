from flask import Blueprint, render_template, flash, jsonify

home = Blueprint('home',__name__)

@home.route("/",methods = ['GET'])
def home_page():
    return render_template('home.html')
