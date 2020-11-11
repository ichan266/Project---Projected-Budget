"""CRUD operations."""

from model import (db, User, Account, EntryLog, connect_to_db) #Bank, RecurrentEntry
from datetime import (date, timedelta)
# from flask_sqlalchemy import SQLAlchemy


### class User ###
def create_user(first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(first_name=first_name, 
                last_name=last_name,
                email=email, 
                password=password)
    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


### class Account ###
def create_account(user_id, account_type, account_nickname):
    """Create and return an account."""

    account = Account(user_id = user_id, 
                      account_type = account_type,
                      account_nickname = account_nickname)
    db.session.add(account)
    db.session.commit()

    return account


def get_account_by_account_id(account_id):
    """Return a specific account info with account_id."""

    return Account.query.filter(Account.account_id == account_id).first()


### class EntryLog ###
def create_entry_log(account_id, date, category, description, amount):
    """Create and return an entry."""

    entry_log = EntryLog(account_id = account_id, 
                         date = date,
                         category = category, 
                         description = description, 
                         amount = amount)
    db.session.add(entry_log)
    db.session.commit()

    return entry_log


def get_entry_logs_by_account_id(account_id):
    """Return all the entry logs associated with a particular account."""

    return EntryLog.query.filter(EntryLog.account_id == account_id).all()


# ### class RecurrentEntry ###
# def create_recurrent_entry(entry_id, start_date, stop_date, frequency):
#     """ Create and return a recurrent entry."""

#     recurrent_entry = RecurrentEntry(entry_id=entry_id,
#                                      start_date=start_date,
#                                      stop_date=stop_date,
#                                      frequency=frequency)
#     db.session.add(recurrent_entry)
#     db.session.commit()

#     return recurrent_entry


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
