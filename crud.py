"""CRUD operations."""

from model import (db, User, Account, EntryLog, connect_to_db)
import datetime
import copy
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


def retrieve_recurrent_entries_by_account_id(account_id):
    """ Find all the recurrent entries and return in a list of object."""

    # Objects are mutable. We need to make a copy of the instances
    copy_of_recurrent_entries = EntryLog.query.filter(EntryLog.account_id == account_id, EntryLog.frequency != None).all()

    return copy_of_recurrent_entries


def find_all_dates(start_date, stop_date, frequency):
    """ Return a list of dates based on one single entry's dates and frequency.
        Frequency is in datetime.timedelta"""

    list_of_dates = []
    while start_date <= stop_date:
        date = start_date + frequency
        if date <= stop_date:
            list_of_dates.append(date)
            start_date = date
        else:
            break

    return list_of_dates


def list_of_recurrent_entries_with_all_dates(list_of_recurrent_entries):
    """ Return a list of recurrent entries associated with all dates based on frequency."""

    updated_entry_list_with_new_dates = []
    
    for entry in list_of_recurrent_entries:
        date = entry.date
        stop_date = entry.stop_date
        frequency = entry.frequency
        list_of_dates = find_all_dates(date, stop_date, frequency)
        for date in list_of_dates:
            entry_copy = copy.deepcopy(entry)
            entry_copy.date = date
            updated_entry_list_with_new_dates.append(entry_copy)

    return updated_entry_list_with_new_dates


if __name__ == '__main__':
    from server import app
    connect_to_db(app)