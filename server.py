"""Server for Projected Budget app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import datetime 

app = Flask(__name__)
app.secret_key = 'dev'
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Render homepage."""

    return render_template('homepage.html')


@app.route('/create_user', methods=['POST'])
def register_user():
    """Create a new user."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    if crud.get_user_by_email(email) != None:
        flash("Account already exists. Please try again.")
    else:
        crud.create_user(first_name, last_name, email, password)
        flash("Account Created!")

    return redirect('/')


@app.route('/confirm_account', methods=['POST'])
def check_account():
    """Confirm account and take user to welcome page."""

    email = request.form['email']
    password = request.form['password']
    user = crud.get_user_by_email(email)
    
    if  user == None or password != user.password:
        flash("Email and password did not match our records. Please try again.")
    else:
        flash('Successfully logged in!')
        session['user_name'] = f'{user.first_name} {user.last_name}'
        session['user_id'] = user.user_id        
        
        print(f"THE SESSION FOR USER NAME IS {session['user_name']}")
        print(f"THE SESSION FOR USER ID IS {session['user_id']}")
        
        #! Can I move this to a different @app.route('/welcome')? # 
        # get all the entry logs associated with a particular account
        entries = crud.get_entry_logs_by_account_id(session['user_id'])

        # use the first entry in entry log's account id to find the type of account
        account = crud.get_account_by_account_id(entries[0].account_id) #it won't work for users with no bank account. 
        account_id = account.account_id
        account_type = account.account_type
        # bank_id = account.bank_id

        # # get the bank name by using bank id from account
        # bank = crud.get_bank_name_by_bank_id(bank_id)
        # bank_name = bank.bank_name

        return render_template('welcome.html', 
                                entries=entries, 
                                account_type=account_type,
                                account_id=account_id) #bank_name=bank_name

    return redirect('/')


# @app.route('/create_bank', methods=['POST'])
# def create_bank():
#     """User to create bank info."""

#     bank_name = request.form['bank_name']
#     bank_code = bank_name[:3].upper()

#     if bank_code

# @app.route('create_transaction', methods=['POST'])
# def create_transaction():
#     """User to create transaction."""

#     account_type = request.form['account_type']
#     date = request.form['transac_date']
#     category = request.form['category']
#     description = request.form['description']
#     amount = request.form['transaction']

    


if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')