"""CRUD operations."""

from model import db, User, Account, Bank, EntryLog, RecurrentEntry


def create_user(first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(first_name=first_name, 
                last_name=last_name,
                email=email, 
                password=password)

    db.session.add(user)
    db.session.commit()

    return user


def create_account(account_type):
    """Create and return an account."""

    account = Account(account_type=account_type)

    db.session.add(account)
    db.session.commit()

    return account


if __name__ == '__main__':
    from server import app
    connect_to_db(app)