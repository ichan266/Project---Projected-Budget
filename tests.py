from unittest import TestCase
import os
from flask_sqlalchemy import SQLAlchemy
import datetime

from server import app
import crud, model


class ProjectTestsHomepage(TestCase):
    """Test homepage."""

    def setUp(self):
        """Setup homepage test."""

        self.client = app.test_client()
        app.config["TESTING"] = True

   
    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn(b"Empower You to Better Foresee Your Financial Future", result.data)


class ProjectTestsLogInProfileAccountDetails(TestCase):
    """Test Login, create new user, and profile page."""

    def setUp(self):
        """Setup database test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = 'key'

        os.system("createdb testpb")
        
        model.connect_to_db(app, "postgresql:///testpb")
        model.db.create_all()
        mock_data()    # def mock_data is close to the bottom of this page


    ### Database ###
    def test_crud_user_in_database(self):
        """Test database by looking up a user by using a function defined in crud."""

        test_user_email = "johnny@john"
        test_user = crud.get_user_by_email(test_user_email)
        self.assertEqual(test_user.user_id, 1)
        self.assertEqual(test_user.email, test_user_email)


    ### Log In Page ###
    def test_successful_login(self):
        """Test login with matched email and password for successful login."""

        result = self.client.post("/confirm_account",
                                  data={"email": "randomly@random", 
                                        "password": "randomly123"},
                                  follow_redirects=True)
        self.assertIn(b"Successfully logged in!", result.data)
        self.assertNotIn(b"Email and password did not match our records.", result.data)
        
    
    def test_failed_login(self):
        """Test login with unmatched email and password for unsuccessful login."""

        result = self.client.post("/confirm_account",
                                  data={"email": "jon@jon", 
                                        "password": "abc"},
                                  follow_redirects=True)
        self.assertIn(b"Email and password did not match our records.", result.data)
        self.assertNotIn(b"Successfully logged in!", result.data)


    def test_successful_creating_new_user(self):
        """Test to successfully create a new user."""

        result = self.client.post("/create_user",
                                  data={"first_name": "Water", 
                                        "last_name": "Melon", 
                                        "email": "water@melon", 
                                        "password": "water123"},
                                  follow_redirects=True)
        self.assertIn(b"Account Created!", result.data)
        self.assertNotIn(b"Account already exists. Please try again.", result.data)


    def test_failed_creating_user(self):
        """Test to unsuccessfully create new account (email already in database)."""

        result = self.client.post("/create_user",
                                  data={"first_name": "Water", 
                                        "last_name": "Melon", 
                                        "email": "johnny@john", 
                                        "password": "water123"},
                                  follow_redirects=True)
        self.assertIn(b"Account already exists. Please try again.", result.data)
        self.assertNotIn(b"Account Created!", result.data)


    ### Profile Page ###
    def test_profile_page(self):
        """Test successful login and redirect to profile page."""

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Jane Doe"
                sess["user_id"] = 2

        result = self.client.get("/profile")
        self.assertIn(b"Hi! Jane Doe", result.data)


    def test_profile_page_with_account_name(self):
        """Test to see if correct account name and account name displays 
        on profile page correctly."""

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Randomly Random"
                sess["user_id"] = 3
        
        result = self.client.get("/profile")
        self.assertIn(b"Hi! Randomly Random", result.data)
        self.assertIn(b"testing3 - Other", result.data)


    def test_profile_page_with_no_account(self):

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Honey Dew"
                sess["user_id"] = 4
        
        result = self.client.get("/profile")
        self.assertIn(b"Hi! Honey Dew", result.data)
        self.assertIn(b"You currently do not have any accounts.", result.data)


    def test_creating_new_account(self):
        """Test to create a new account. 
            Note: issues with spaces in assertIn. Searched for one keyword for now."""

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Honey Dew"
                sess["user_id"] = 4

        result = self.client.post("/create_account",
                                  data={"account_type": "Saving", 
                                        "account_nickname": "Honey's first account"},
                                  follow_redirects=True)
        self.assertIn(b"first", result.data)
        self.assertNotIn(b"Please add an account.", result.data)


    ### Acount Details Page ###
    def test_entries_displayed(self):
        """Test if entries is displayed correctly with correct user."""

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Johnny John"
                sess["user_id"] = 1

        result = self.client.get("/profile/1",
                                 data={"account_id": 1},
                                 follow_redirects=True)
        self.assertIn(b"Account ID: 1", result.data)
        self.assertIn(b"Saving", result.data)
        self.assertIn(b"500", result.data)


    def test_creating_new_transaction(self):
        """Test to create a new transaction."""

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Jane Doe"
                sess["user_id"] = 2
        today = datetime.date.today()

        result = self.client.post("/create_transaction",
                                 data={"account_id": 2, 
                                       "date": today, 
                                       "category": "Saving", 
                                       "description": "unittest",
                                       "amount": 12345, 
                                       "frequency_int": 0,
                                       "frequency_unit": "days"},
                                 follow_redirects=True)
        self.assertIn(b"12345", result.data)
        self.assertIn(b"unittest", result.data)


    ### Removal ###
    """ Note: Due to use of confirmation windows with JavaScript, 
        removal of account and entry are tested using functions defined in crud.py."""

    #* Remove Account *#
    def test_crud_removing_account(self):
        """Test for removing an account with a function in crud."""

        crud.remove_account_by_account_id(1)
        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Johnny John"
                sess["user_id"] = 1

        result = self.client.get("/profile")
        self.assertIn(b"Hi! Johnny John", result.data)
        self.assertNotIn(b"testing1", result.data)
      
    #* Remove Entry *#
    def test_crud_removing_entry(self):
        """Test for removing an entry with a function in crud."""

        crud.remove_entry_by_entry_id(2)
        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Jane Doe"
                sess["user_id"] = 2

        result = self.client.get("/profile/2")
        self.assertIn(b"Jane", result.data)
        self.assertNotIn(b"testing2", result.data)


    ### Log Out ###
    def test_logout(self):
        """Test logout route."""

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Randomly Random"
                sess["user_id"] = 3

            result = self.client.get("/logout", follow_redirects=True)

            self.assertNotIn(b'user_name', sess)
            self.assertNotIn(b"user_id", sess)
            self.assertIn(b'You are logged out.', result.data)
    
    
    def tearDown(self):
        """Tear down test."""

        model.db.session.remove()
        model.db.drop_all()
        model.db.engine.dispose()
        os.system("dropdb testpb")


def mock_data():
    """Create sample data for testing."""

    crud.create_user("Johnny", "John", "johnny@john", "john123")
    crud.create_user("Jane", "Doe", "jane@doe", "jane123")
    crud.create_user("Randomly", "Random", "randomly@random", "randomly123")
    crud.create_user("Honey", "Dew", "honey@dew", "honey123")

    crud.create_account(1, "Saving", "testing1")
    crud.create_account(2, "Checking", "testing2")
    crud.create_account(3, "Other", "testing3")

    n = datetime.date.today()
    future_date = datetime.date.today() + datetime.timedelta(120)

    crud.create_entry_log(1, n, "Income", "testing1: x1", 500)
    crud.create_entry_log(2, n, "Income", "testing2: with q20Days", 1000, future_date, datetime.timedelta(20))
    crud.create_entry_log(3, n, "Expense", "desc-testing3", -500)


# Automate all test
if __name__ == "__main__":
    import unittest
   
    unittest.main()