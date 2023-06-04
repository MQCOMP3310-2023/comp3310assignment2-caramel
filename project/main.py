from flask import Blueprint, render_template, request, flash, redirect, url_for, g
from .models import Restaurant, MenuItem, User
from sqlalchemy import asc
from . import db
from .forms import LoginForm, RegisterForm
from flask_login import login_user, current_user, login_required, logout_user

main = Blueprint('main', __name__)

# Source: https://github.com/marcelomd/flask-wtf-login-example/blob/master/app/views.py
@main.before_request
def before_request():
    g.user = current_user

#Show all restaurants
@main.route('/')
@main.route('/restaurant/')
def showRestaurants():
   #  logging.info( "Show resturants" )
  restaurants = db.session.query(Restaurant).order_by(asc(Restaurant.name))
  return render_template('restaurants.html', restaurants = restaurants)

#Create a new restaurant
@main.route('/restaurant/new/', methods=['GET','POST'])
@login_required
def newRestaurant():
   #  logging.info( "adding resturant" )
  if request.method == 'POST':
      newRestaurant = Restaurant(name = request.form['name'])
      db.session.add(newRestaurant)
      flash('New Restaurant %s Successfully Created' % newRestaurant.name)
      db.session.commit()
      return redirect(url_for('main.showRestaurants'))
  else:
      return render_template('newRestaurant.html')

#Edit a restaurant
@main.route('/restaurant/<int:restaurant_id>/edit/', methods = ['GET', 'POST'])
@login_required
def editRestaurant(restaurant_id):
  #  logging.info( "editing resturant: " + resturant_id )
  editedRestaurant = db.session.query(Restaurant).filter_by(id = restaurant_id).one()
  if request.method == 'POST':
      if request.form['name']:
        editedRestaurant.name = request.form['name']
        flash('Restaurant Successfully Edited %s' % editedRestaurant.name)
        return redirect(url_for('main.showRestaurants'))
  else:
    return render_template('editRestaurant.html', restaurant = editedRestaurant)


#Delete a restaurant
@main.route('/restaurant/<int:restaurant_id>/delete/', methods = ['GET','POST'])
@login_required
def deleteRestaurant(restaurant_id):
  restaurantToDelete = db.session.query(Restaurant).filter_by(id = restaurant_id).one()
  if request.method == 'POST':
    #  logging.info( "deleting resturant: "+ resturant_id )
    db.session.delete(restaurantToDelete)
    flash('%s Successfully Deleted' % restaurantToDelete.name)
    db.session.commit()
    return redirect(url_for('main.showRestaurants', restaurant_id = restaurant_id))
  else:
    return render_template('deleteRestaurant.html',restaurant = restaurantToDelete)

#Show a restaurant menu
@main.route('/restaurant/<int:restaurant_id>/')
@main.route('/restaurant/<int:restaurant_id>/menu/')


def showMenu(restaurant_id):
    #  logging.info( "Show Menu" )
    restaurant = db.session.query(Restaurant).filter_by(id = restaurant_id).one()
    items = db.session.query(MenuItem).filter_by(restaurant_id = restaurant_id).all()
    return render_template('menu.html', items = items, restaurant = restaurant)

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # Get the search query from the request URL parameters

    if not query:
        flash('Please enter a search query')
        return redirect(url_for('main.showRestaurants'))
    
#  logging.info( "searching for: " + query )

    #TODO
    # query needs to be sanitised to ensure that the input field cannot be used for any kind of code injection. 
    

    
    # Query the database for matching restaurants and menu items
    restaurants = db.session.query(Restaurant).filter(Restaurant.name.ilike(f'%{query}%')).order_by(asc(Restaurant.name)).all()
    menu_items = db.session.query(MenuItem).filter(MenuItem.name.ilike(f'%{query}%')).all()

    # Render the search results template with the matching restaurants and menu items
    return render_template('search_results.html', query=query, restaurants=restaurants, menu_items=menu_items)


# Show a restaurant
@main.route('/restaurant/<int:restaurant_id>/')
def showRestaurant(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).first()
    return render_template('restaurant.html', restaurant=restaurant)


# Show a menu item
@main.route('/menu/<int:menu_item_id>/')
def showMenuItem(menu_item_id):
    menu_item = db.session.query(MenuItem).filter_by(id=menu_item_id).first()
    return render_template('menu_item.html', menu_item=menu_item)


#Create a new menu item
@main.route('/restaurant/<int:restaurant_id>/menu/new/',methods=['GET','POST'])
@login_required
def newMenuItem(restaurant_id):
  restaurant = db.session.query(Restaurant).filter_by(id = restaurant_id).one()
  if request.method == 'POST':
      newItem = MenuItem(name = request.form['name'], description = request.form['description'], price = request.form['price'], course = request.form['course'], restaurant_id = restaurant_id)
      db.session.add(newItem)
      db.session.commit()
      flash('New Menu %s Item Successfully Created' % (newItem.name))
      return redirect(url_for('main.showMenu', restaurant_id = restaurant_id))
  else:
      return render_template('newmenuitem.html', restaurant_id = restaurant_id)

#Edit a menu item
@main.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET','POST'])
@login_required
def editMenuItem(restaurant_id, menu_id):

    editedItem = db.session.query(MenuItem).filter_by(id = menu_id).one()
    restaurant = db.session.query(Restaurant).filter_by(id = restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        db.session.add(editedItem)
        db.session.commit() 
        flash('Menu Item Successfully Edited')
        return redirect(url_for('main.showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id = restaurant_id, menu_id = menu_id, item = editedItem)


#Delete a menu item

@main.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods = ['GET','POST'])
@login_required
def deleteMenuItem(restaurant_id,menu_id):
    restaurant = db.session.query(Restaurant).filter_by(id = restaurant_id).one()
    itemToDelete = db.session.query(MenuItem).filter_by(id = menu_id).one() 
    if request.method == 'POST':
        db.session.delete(itemToDelete)
        db.session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('main.showMenu', restaurant_id = restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item = itemToDelete)

# Source: https://github.com/marcelomd/flask-wtf-login-example/blob/master/app/views.py
@main.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form, csrf_enabled=False)
    if form.validate():
        new_user = User(email=form.email.data,
                username=form.username.data,
                password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

# Source: https://github.com/marcelomd/flask-wtf-login-example/blob/master/app/views.py
@main.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            redirect_url = request.args.get('next') or url_for('main.showRestaurants')
            return redirect(redirect_url)
    return render_template('login.html', form=form)

# Source: https://github.com/marcelomd/flask-wtf-login-example/blob/master/app/views.py
@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.showRestaurants'))