"""Models for Projected Budget app."""

from flask_sqlalchemy import SQLAlchemy
from datetime import (datetime, date, timedelta)
from datetime import date

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
    password = db.Column(db.String, nullable=False)    

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
    date = db.Column(db.Date)
    category = db.Column(db.String)
    description = db.Column(db.String)
    amount = db.Column(db.Integer)

    accounts = db.relationship('Account')
    # recurrent_entries = db.relationship('RecurrentEntry')

    def __repr__(self):
        return f'<Entry Log: entry_id={self.entry_id}, account_id={self.account_id}, date={self.date}, category={self.category}, description={self.description}, amount={self.amount}>'


# class RecurrentEntry(db.Model):
#     """A recurrent entry."""

#     __tablename__ = 'recurrent_entries'

#     recurrent_id = db.Column(db.Integer,
#                              primary_key=True,
#                              autoincrement=True
#                              )
#     entry_id = db.Column(db.Integer, db.ForeignKey('entry_logs.entry_id'))
#     start_date = db.Column(db.Date)
#     stop_date = db.Column(db.Date)
#     frequency = db.Column(db.Interval) # Interval is equivalent to datetime.timedelta

#     entry_logs = db.relationship('EntryLog')

#     def __repr__(self):
#         return f'<Recurrent Entry: recurrent_id={self.recurrent_id}, 
#                   entry_id={self.entry_id}, Start Date={self.start_date}, 
#                   Stop Date ={self.stop_date}, Frequency={self.frequency}>'


def connect_to_db(flask_app, db_uri='postgresql:///pb', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)