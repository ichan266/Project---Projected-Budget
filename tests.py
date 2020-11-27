import unittest
from model import User
from flask_sqlalchemy import SQLAlchemy
from datetime import (datetime, date, timedelta)
from datetime import date

db = SQLAlchemy()


def test_new_user():
    """GIVEN a User model 
       WHEN a new User is created
       THEN check first name, last name, email, and password fields are defined correctly
    """

    user = User(first_name="Jane", last_name="Doe", email="123@123", password="12345")
    assert user.first_name == "Jane"
    assert user.last_name == "Doe"
    assert user.email == "123@123"
    assert user.password == "12345"
