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

    create_user("Bob1", "Bobby1", "test@test1", "test1")
    create_user("Bob2", "Bobby2", "test@test2", "test2")
    create_user("Bob3", "Bobby3", "test@test3", "test3")
    create_user("Bob4", "Bobby4", "test@test4", "test4")

    create_bank("CAP", "Capital One")
    create_bank("BOA", "Bank of America")
    create_bank("JPM", "JP Morgan Chase")
    create_bank("WFA", "Wells Fargo")

    create_account(1,1,"checking")
    create_account(4,3,"checking")