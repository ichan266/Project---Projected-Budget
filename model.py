"""Models for Projected Budget app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import (datetime, date, timedelta)
from datetime import date
import os
import sys
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True,
                        )
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)  # 'd password value

    def __init__(self, first_name, last_name, email, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(
            method='pbkdf2:sha512:150000', password=password
        )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    accounts = db.relationship('Account')

    def __repr__(self):
        return f'<User: user_id={self.user_id}, User Name={self.first_name} {self.last_name}, email={self.email}>'


class Account(db.Model):
    """An account."""

    __tablename__ = 'accounts'

    account_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True
                           )
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    account_type = db.Column(db.String)
    account_nickname = db.Column(db.String)

    users = db.relationship('User')
    entry_logs = db.relationship('EntryLog')

    def __repr__(self):
        return f'<Account: account_id={self.account_id}, user id={self.user_id}, account type={self.account_type}>'


class EntryLog(db.Model):
    """An account entry."""

    __tablename__ = 'entry_logs'

    entry_id = db.Column(db.Integer,
                         primary_key=True,
                         autoincrement=True
                         )
    account_id = db.Column(db.Integer, db.ForeignKey('accounts.account_id'))
    date = db.Column(db.Date, nullable=False)
    category = db.Column(db.String)
    description = db.Column(db.String)
    amount = db.Column(db.Integer)
    stop_date = db.Column(db.Date, nullable=True)  # new for recurrent entries
    # new for recurrent entries
    frequency = db.Column(db.Interval, nullable=True)

    accounts = db.relationship('Account')

    def __repr__(self):
        return f'<Entry Log: entry_id={self.entry_id}, account_id={self.account_id}, date={self.date}, category={self.category}, description={self.description}, amount={self.amount}, stop date={self.stop_date}, frequency={self.frequency}>'


def connect_to_db(flask_app, echo=True, local=False):

    if local:
        pguser = os.environ.get("USER-pg")
        pgpassword = os.environ.get("PASSWORD-pg")
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + \
            pguser + ':' + pgpassword + '@localhost:5432/pb'
    else:
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "DATABASE_URL")

    # flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app
    local = "-local" in sys.argv
    connect_to_db(app, local=local)
