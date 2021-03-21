"""Script to seed database."""

import os
import sys
# import json
import datetime
# import calendar

import crud
import model
from model import (User, Account, EntryLog, db, connect_to_db)
import server


local = "-local" in sys.argv

if "-resetdb" in sys.argv:
    os.system('dropdb pb')
    os.system('createdb pb')

connect_to_db(server.app, local=local)
db.create_all()


### Seeding User ###
for n in range(1, 11):
    """Seeding users table."""

    first_name = f'Bob{n}'
    last_name = f'Bobby{n}'
    email = f'test{n}@test.com'  # A unique email!
    password = f'test{n}'
    crud.create_user(first_name, last_name, email, password)

#* Miss Piggy *#
crud.create_user("Miss", "Piggy", "MsPiggy@muppets.com", "kermit")

### Seeding Account ###
for n in range(1, 5):
    """Seeding accounts table for user_id 1."""

    user_id = 1
    account_type = "Checking"
    account_nickname = f"Nickname{n}"
    crud.create_account(user_id, account_type, account_nickname)


for n in range(5, 9):
    """Seeding accounts table for user_id 2."""

    user_id = 2
    account_type = "Checking"
    account_nickname = f"Nickname{n}"
    crud.create_account(user_id, account_type, account_nickname)

#@ Miss Piggy @#
crud.create_account(11, "Checking", "Wedding Fund")  # account id = 10
# crud.create_account(11, "Checking", "Shopping - Clothes")
# crud.create_account(11, "Checking", "Shopping - Jewelries")  # account id = 12
# crud.create_account(11, "Checking", "Shopping - MakeUp")


### Seeding EntryLog ###
for n in range(1, 5):
    """Seeding entry_logs table with account_id #1."""
    account_id = 1
    date = datetime.date.today() + datetime.timedelta(days=n*10)
    category = 'Income'
    description = f'trial {n}'
    amount = 1000 + (n*100)
    crud.create_entry_log(account_id,
                          date,
                          category,
                          description,
                          amount)

for n in range(5, 10):
    """Seeding entry_logs table with account_id #2."""
    account_id = 2
    date = datetime.date.today() + datetime.timedelta(days=n*21)
    category = 'Income'
    description = f'trial {n}'
    amount = 2000 + (n*200)
    crud.create_entry_log(account_id,
                          date,
                          category,
                          description,
                          amount)

for n in range(11, 15):
    """Seeding recurrent entries into entry_logs table with account_id #3."""
    account_id = 8
    date = datetime.date.today() + datetime.timedelta(n)
    category = 'Income'
    description = f'trial {n}'
    amount = 10000 + (n*200)
    stop_date = datetime.date.today() + datetime.timedelta(days=n+80)
    # ? SQL Alchemy will change this to days
    frequency = datetime.timedelta(weeks=2)
    crud.create_entry_log(account_id,
                          date,
                          category,
                          description,
                          amount,
                          stop_date,
                          frequency)

#@ Miss Piggy @#
crud.create_entry_log(9, datetime.date.today(), "Income", "Gig", 10000)
crud.create_entry_log(9, datetime.date.today(),
                      "Expense", "Venue", -20000)
crud.create_entry_log(9, (datetime.date.today() + datetime.timedelta(days=30)),
                      "Expense", "Flowers", -3000)
crud.create_entry_log(9, (datetime.date.today() + datetime.timedelta(days=10)), "Expense",
                      "Pretty Clothes", -3000, (datetime.date.today() + datetime.timedelta(days=120)), datetime.timedelta(30))
crud.create_entry_log(9, (datetime.date.today() +
                          datetime.timedelta(days=40)), "Expense", "Makeup", -3000)
crud.create_entry_log(9, (datetime.date.today() +
                          datetime.timedelta(days=50)), "Expense", "Band", -6000)
crud.create_entry_log(9, (datetime.date.today() +
                          datetime.timedelta(days=120)), "Income", "Sell the Theater", 100000)
