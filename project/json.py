from flask import Blueprint, jsonify
from .models import Restaurant, MenuItem
from sqlalchemy import text
from . import db
import json as pyjs

json = Blueprint('json', __name__)

#JSON APIs to view Restaurant Information
@json.route('/restaurant/<restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    items = db.session.execute(text('SELECT * FROM menu_item WHERE restaurant_id = %s', restaurant_id))
# Adjusted the user input string to query parameter to avoid SQL injection.
    items_list = [ i._asdict() for i in items ]
    return pyjs.dumps(items_list)

@json.route('/restaurant/<restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
    Menu_Item = db.session.execute(text('SELECT * FROM menu_item WHERE id = %d LIMIT 1', menu_id))
# Set up a query parameter in code to avoid SQL injection attacks. Used placeholder instead of concatenating
# the user input variable.
    items_list = [ i._asdict() for i in Menu_Item ]
    return pyjs.dumps(items_list)

@json.route('/restaurant/JSON')
def restaurantsJSON():
    restaurants = db.session.execute(text('select * from restaurant'))
    rest_list = [ r._asdict() for r in restaurants ]
    return pyjs.dumps(rest_list)


