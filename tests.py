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
        self.assertIn(b"Welcome to My First Project Website!", result.data)


class ProjectTestsDatabaseAndProfile(TestCase):
    """Test database."""

    def setUp(self):
        """Setup database test."""

        self.client = app.test_client()
        app.config["TESTING"] = True
        app.config["SECRET_KEY"] = 'key'

        os.system("createdb testpb")
        
        model.connect_to_db(app, "postgresql:///testpb")

        model.db.create_all()
        mock_data()

        with self.client as test_client:
            with test_client.session_transaction() as sess:
                sess["user_name"] = "Jane Doe"
                sess["user_id"] = 2

    def test_profile_page(self):
        """Test profile page."""

        result = self.client.get("/profile")
        self.assertIn(b"Hi! Jane Doe", result.data)  
   
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

    crud.create_account(1, "Saving", "testing1")
    crud.create_account(2, "Checking", "testing2")
    crud.create_account(3, "Other", "testing3")

    n = datetime.date.today()

    crud.create_entry_log(1, n, "Income", "desc-testing1", 500)
    crud.create_entry_log(2, n, "Income", "desc-testing2", 1000, datetime.date(2021, 3, 31), datetime.timedelta(20))
    crud.create_entry_log(3, n, "Income", "desc-testing3", -500)


# Automate all test
if __name__ == "__main__":
    import unittest
   
    unittest.main()