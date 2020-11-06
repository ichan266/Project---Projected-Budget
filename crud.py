"""CRUD operations."""

from model import db, User, Bank, Account, connect_to_db # EntryLog, RecurrentEntry
from flask_sqlalchemy import SQLAlchemy


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
    """Create and return an account."""

    bank = Bank(bank_code=bank_code, bank_name=bank_name)

    db.session.add(bank)
    db.session.commit()

    return bank


def create_account(user_id, bank_id, account_type):
    """Create and return an account."""

    account = Account(user_id=user_id, bank_id=bank_id ,account_type=account_type)

    db.session.add(account)
    db.session.commit()

    return account


def create_entry_log(account_id, date, category, description, amount):
    """Create and return an account."""

    entry_log = EntryLog(account_id=account_id, date=date ,category=category, description=description, amount=amount)

    db.session.add(entry_log)
    db.session.commit()

    return entry_log


if __name__ == '__main__':
    from server import app

    connect_to_db(app)
    db.create_all()



    create_account(1,1,"checking")
    create_account(4,3,"checking")