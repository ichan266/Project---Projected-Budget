"""CRUD operations."""

from model import db, User, Bank, Account, EntryLog, RecurrentEntry, connect_to_db
from datetime import (date, timedelta)
# from flask_sqlalchemy import SQLAlchemy


def create_user(first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(first_name=first_name, 
                last_name=last_name,
                email=email, 
                password=password)
    db.session.add(user)
    db.session.commit()

    return user


def create_bank(bank_code, bank_name):
    """Create and return a bank."""

    bank = Bank(bank_code=bank_code, 
                bank_name=bank_name)
    db.session.add(bank)
    db.session.commit()

    return bank


def create_account(user_id, bank_id, account_type):
    """Create and return an account."""

    account = Account(user_id = user_id, 
                      bank_id = bank_id ,
                      account_type = account_type)
    db.session.add(account)
    db.session.commit()

    return account


def create_entry_log(account_id, date, category, description, amount):
    """Create and return an entry."""

    entry_log = EntryLog(account_id = account_id, 
                         date = date ,
                         category = category, 
                         description = description, 
                         amount = amount)
    db.session.add(entry_log)
    db.session.commit()

    return entry_log


def create_recurrent_entry(entry_id, start_date, stop_date, frequency):
    """ Create and return a recurrent entry."""

    recurrent_entry = RecurrentEntry(entry_id = entry_id,
                                     start_date = start_date,
                                     stop_date = stop_date,
                                     frequency = frequency)
    db.session.add(recurrent_entry)
    db.session.commit()

    return recurrent_entry


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
