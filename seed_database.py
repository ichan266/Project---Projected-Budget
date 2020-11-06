"""Script to seed database."""

import os
# import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb pb')
os.system('createdb pb')

model.connect_to_db(server.app)
model.db.create_all()

for n in range(1,11):
    """Seeding the table, users."""
    first_name = f'Bob{n}'
    last_name = f'Bobby{n}'
    email = f'user{n}@test.com' # A unique email!
    password = f'test{n}'
    crud.create_user(first_name, last_name, email, password)

crud.create_bank("CAP", "Capital One")
crud.create_bank("BOA", "Bank of America")
crud.create_bank("JPM", "JP Morgan Chase")
crud.create_bank("WFA", "Wells Fargo")

for n in range(1,5):
    """Seeding the table, accounts."""
    user_id = n
    bank_id = n
    account_type = f'Checking{n}'
    crud.create_account(user_id, bank_id, account_type)

for n in range (1,5):
    """ Seeding the table, entry_logs."""
    account_id = n
    date = f'11-{n+6}-20'
    category = f'Income{n}'
    description = f'trial {n}'
    amount = 1000 + (n*100)
    crud.create_entry_log(account_id, 
                          date, 
                          category, 
                          description, 
                          amount)

                          