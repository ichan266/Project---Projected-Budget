"""CRUD operations."""

from model import (db, User, Account, EntryLog, connect_to_db)
import datetime
# from flask_sqlalchemy import SQLAlchemy


##### class User #####
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


##### class Account #####
def create_account(user_id, account_type, account_nickname):
    """Create and return an account."""

    account = Account(user_id = user_id, 
                      account_type = account_type,
                      account_nickname = account_nickname)
    db.session.add(account)
    db.session.commit()

    return account


def get_accounts_by_user_id(user_id):
    """Return a list of accounts by searching with user_id."""

    return Account.query.filter(Account.user_id == user_id).all()


def get_account_by_account_id(account_id):
    """Return a specific account info with account_id."""

    return Account.query.filter(Account.account_id == account_id).first()


def remove_account_by_account_id(account_id):
    """Remove an account by account_id. 
       Note: this action will remove account even if there are entries in it."""

    EntryLog.query.filter(EntryLog.account_id == account_id).delete()
    db.session.commit()
    Account.query.filter(Account.account_id == account_id).delete()
    db.session.commit()


##### class EntryLog #####
def create_entry_log(account_id, date, category, description, amount, stop_date=None, frequency=None):
    """Create and return an entry."""

    entry_log = EntryLog(account_id = account_id, 
                         date = date,
                         category = category, 
                         description = description, 
                         amount = amount,
                         stop_date = stop_date,
                         frequency = frequency) #! stop_date and frequency added to consolidate tables
    db.session.add(entry_log)
    db.session.commit()

    return entry_log


def get_entry_logs_by_account_id(account_id):
    """Return all the entry logs associated with a particular account."""

    return EntryLog.query.filter(EntryLog.account_id == account_id).all()


def sort_entry_logs(account_id):
    """Return entry logs sorted by date."""

    return EntryLog.query.filter(EntryLog.account_id == account_id).order_by("date").all()


def remove_entry_by_entry_id(entry_id):
    """Remove an entry by entry_id."""

    EntryLog.query.filter(EntryLog.entry_id == entry_id).delete()
    db.session.commit()


#* recurrent entries *#
def convert_frequency_to_num_of_day(frequency_int, frequency_unit):
    """Return # of days from # of weeks for or just # of days in timedelta 
        for recurrent entries."""
    
    if frequency_unit == "weeks":
        num_of_days = 7 * frequency_int
    elif frequency_unit == "days":
        num_of_days = frequency_int

    return datetime.timedelta(num_of_days)


def retrieve_newest_entry():
    """ Use it to find the entry_id for the newest entry."""

    last_entry = EntryLog.query.all()[-1]
    entry_id = last_entry.entry_id

    return entry_id


# def get_entry_logs_by_entry_id(entry_id): #! How?


def list_dates(start_date, stop_date, frequency): #frequency in datetime.timedelta
    """If recurrent entries, return a list of dates."""

    list_of_dates = []
    while start_date <= stop_date:
        date = start_date + frequency
        if date <= stop_date:
            list_of_dates.append(date)
            start_date = date
        else:
            break

    return list_of_dates


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
