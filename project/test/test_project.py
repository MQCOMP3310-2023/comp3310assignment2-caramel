#unit tests stubs generated from https://studio.cucumber.io

#TODO need to implement the unit test stubs below
#the scenarios in these unit tests are for testing the authentication mechanism. 
#They are tests for testing the access privileges of the different users including admin users, resturant owner users and public users. 

# encoding: UTF-8
import unittest
from actionwords import Actionwords

class TestComp3310TestWriting(unittest.TestCase):
    def setUp(self):
        self.actionwords = Actionwords(self)

    def test_user_auth(self):
        pass

    def authentication_test_for_admin(self):
        self.actionwords.feature_admin_login()
        self.actionwords.scenario_as_a_administator_i_want_to_log_in_successfully_with_the_correct_privilidges()
        # Given the user is on the home page
        self.actionwords.the_user_is_on_the_home_page()
        # And the user is an admin
        self.actionwords.the_user_is_an_admin()
        # And the user has typed their correct username and password into the appropriate authenntication boxes
        self.actionwords.the_user_has_typed_their_correct_username_and_password_into_the_appropriate_authenntication_boxes()
        # And the user has clicked on the sign in button
        self.actionwords.the_user_has_clicked_on_the_sign_in_button()
        # Then the user should be authenticated as an admin
        self.actionwords.the_user_should_be_authenticated_as_an_admin()
        # Given the user has been authenticated as admin
        self.actionwords.the_user_has_been_authenticated_as_admin()
        # Then the successful login message ("Logged in as admin") should be displayed
        self.actionwords.the_successful_login_message_logged_in_as_admin_should_be_displayed(logged_in_as_admin = "Logged in as admin")
        # And the admin should beable to add restaurant owners,restuarants and menu items
        self.actionwords.the_admin_should_beable_to_add_restaurant_ownersrestuarants_and_menu_items()
        # And the admin should beable to edit restaurant owners, restaurants and menu items
        self.actionwords.the_admin_should_beable_to_edit_restaurant_owners_restaurants_and_menu_items()
        # And the admin should be able to delete restaurant owners, restaurants and menu items
        self.actionwords.the_admin_should_be_able_to_delete_restaurant_owners_restaurants_and_menu_items()

    def test_authentication_test_for_admin_first_one(self):
        self.authentication_test_for_admin()



    def authentication_test_for_restaurant_owners(self):
        self.actionwords.feature_resturant_owner_login()
        self.actionwords.scenario_a_resturant_owner_should_beable_to_log_in_successfully_with_the_correct_privilidges()
        # Given the user is on the home page
        self.actionwords.the_user_is_on_the_home_page()
        # And the user is a Resturant Owner
        self.actionwords.the_user_is_a_resturant_owner()
        # And the user has typed their correct username and password into the appropriate authenntication boxes
        self.actionwords.the_user_has_typed_their_correct_username_and_password_into_the_appropriate_authenntication_boxes()
        # And the user has clicked on the sign in button
        self.actionwords.the_user_has_clicked_on_the_sign_in_button()
        # Then the user should be authenticated as a Resturant Owner
        self.actionwords.the_user_should_be_authenticated_as_a_resturant_owner()
        # Given the user has been authenticated as a Resturant Owner
        self.actionwords.the_user_has_been_authenticated_as_a_resturant_owner()
        # Then the login message successfully logged in as restaurant owner should be displayed "Logged in as admin"
        self.actionwords.the_login_message_successfully_logged_in_as_restaurant_owner_should_be_displayed(logged_in_as_resturant_owner = "Logged in as resturant owner")
        # And the Resturant Owner should be able to add restuarants and menu items
        self.actionwords.the_resturant_owner_should_be_able_to_add_restuarants_and_menu_items()
        # And the resturant owner shoule be able to edit restaurants and menu items
        self.actionwords.the_resturant_owner_shoule_be_able_to_edit_restaurants_and_menu_items()
        # And the resturant owner shoule be able to delete restaurants and menu items
        self.actionwords.the_resturant_owner_shoule_be_able_to_delete_restaurants_and_menu_items()

    def test_authentication_test_for_restaurant_owners_first_one(self):
        self.authentication_test_for_restaurant_owners()



    def authentication_test_for_public_users(self):
        self.actionwords.feature_public_user_login()
        self.actionwords.scenario_a_public_user_should_beable_to_log_in_successfully_with_the_correct_privilidges()
        # Given the user is on the home page
        self.actionwords.the_user_is_on_the_home_page()
        # And the user is a Public User
        self.actionwords.the_user_is_a_public_user()
        # And the user has typed their correct username and password into the appropriate authenntication boxes
        self.actionwords.the_user_has_typed_their_correct_username_and_password_into_the_appropriate_authenntication_boxes()
        # And the user has clicked on the sign in button
        self.actionwords.the_user_has_clicked_on_the_sign_in_button()
        # Then the user should be authenticated as a Public User
        self.actionwords.the_user_should_be_authenticated_as_a_public_user()
        # Given the user has been authenticated as a Public User
        self.actionwords.the_user_has_been_authenticated_as_a_public_user()
        # Then the login message successfully logged in as Public User should be displayed "Logged in as admin"
        self.actionwords.the_login_message_successfully_logged_in_as_public_user_should_be_displayed(logged_in_as_resturant_owner = "Logged in as public user")
        # And the Public Users should be able to view restuarants and menu items
        self.actionwords.the_public_users_should_be_able_to_view_restuarants_and_menu_items()

    def test_authentication_test_for_public_users_first_one(self):
        self.authentication_test_for_public_users()
