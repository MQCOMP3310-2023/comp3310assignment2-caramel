#import logging
from flask import Blueprint, jsonify
from .models import Restaurant, MenuItem
from sqlalchemy import text
from . import db
import json as pyjs     
# OWASP top 10 vulnerability number 6. Vulnerable and Outdated Components
   # these import statemnts demonstrate a vulnerability in that the
#application is reliant on thid party libaries in order to function. 
#if these are not updated or old and outdated versions are used then this may present a significant risk to the application.
# Therfore, It is essential to make sure that these imported libaries are up to date as they present a significant, yet unobvious vulnerability to the system. 




json = Blueprint('json', __name__)

#JSON APIs to view Restaurant Information
@json.route('/restaurant/<restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
  #  logging.info( "Selecting resturant:" + restaurant_id )
    items = db.session.execute(text('SELECT * FROM menu_item WHERE restaurant_id = %d', restaurant_id))
# Adjusted the user input string to query parameter to avoid SQL injection.
    items_list = [ i._asdict() for i in items ]
    return pyjs.dumps(items_list)

#It would be a good idea to implement log functions here.
# this will mean that it is possible to see the restuarnt id after it has been created 



@json.route('/restaurant/<restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
     #  logging.info( "Selecting menu:" + menu_id )
    Menu_Item = db.session.execute(text('SELECT * FROM menu_item WHERE id = %d LIMIT 1', menu_id))
# Set up a query parameter in code to avoid SQL injection attacks. Used placeholder instead of concatenating
# the user input variable.
    items_list = [ i._asdict() for i in Menu_Item ]
    return pyjs.dumps(items_list)

@json.route('/restaurant/JSON')
def restaurantsJSON():
     #  logging.info( "Selecting all resturants")
    restaurants = db.session.execute(text('select * from restaurant'))
    rest_list = [ r._asdict() for r in restaurants ]
    return pyjs.dumps(rest_list)


