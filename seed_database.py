"""Script to seed database."""

import os
# import json
import datetime
import calendar

import crud
import model
import server

os.system('dropdb pb')
os.system('createdb pb')

model.connect_to_db(server.app)
model.db.create_all()

for n in range(1,11):
    """Seeding users table."""
    
    first_name = f'Bob{n}'
    last_name = f'Bobby{n}'
    email = f'test{n}@test.com' # A unique email!
    password = f'test{n}'
    crud.create_user(first_name, last_name, email, password)

crud.create_bank("CAP", "Capital One")
crud.create_bank("BOA", "Bank of America")
crud.create_bank("JPM", "JP Morgan Chase")
crud.create_bank("WFA", "Wells Fargo")

for n in range(1,5):
    """Seeding accounts table."""
    
    user_id = 1
    bank_id = 2
    account_type = 'Checking'
    crud.create_account(user_id, bank_id, account_type)

for n in range (1,5):
    """Seeding entry_logs table."""
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

for n in range (5,10):
    """Seeding entry_logs table."""
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

for n in range (1,5):
    """Seeding recurrent_entries table."""

    entry_id = n
    today = datetime.date.today()
    start_date = today + datetime.timedelta(days=n)
    frequency = 100
    stop_date = start_date + datetime.timedelta(days=frequency)
    crud.create_recurrent_entry(entry_id,
                                start_date,
                                stop_date,
                                frequency)