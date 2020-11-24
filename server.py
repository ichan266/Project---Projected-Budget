"""Server for Projected Budget app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined
import datetime
import os

app = Flask(__name__)
if "SECRET_KEY" in os.environ:
    app.secret_key = os.environ["SECRET_KEY"]
else:
    app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined
# In order to use the secret key, I need to type in "source secrets.sh"
# in the terminal before I start the server

@app.route("/")
def homepage():
    """Render homepage."""

    return render_template("homepage.html")


@app.route("/confirm_account", methods=["POST"])
def check_account():
    """Confirm account and take user to welcome page."""

    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)
    
    if  user == None or password != user.password:
        flash("Email and password did not match our records. Please try again.")
    else:
        flash("Successfully logged in!")
        session['user_name'] = f"{user.first_name} {user.last_name}"
        session['user_id'] = user.user_id
        
        print(f"THE SESSION FOR USER NAME IS {session['user_name']}")
        print(f"THE SESSION FOR USER ID IS {session['user_id']}")
        print(f"THE SESSION IS {session}")
        
        # accounts = crud.get_accounts_by_user_id(session['user_id'])

        # return render_template("profile.html", accounts=accounts)

        return redirect("/profile")

    return redirect("/")


@app.route("/create_user", methods=["POST"])
def register_user():
    """Create a new user."""

    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")

    if crud.get_user_by_email(email) != None:
        flash("Account already exists. Please try again.")
    else:
        user = crud.create_user(first_name, last_name, email, password)
        session['user_name'] = f"{user.first_name} {user.last_name}"
        session['user_id'] = user.user_id
        flash("Account Created!")
        return redirect("/profile")

    return redirect("/")


@app.route("/profile")
def show_profile():
    """Show user profile with all user's accounts."""

    accounts = crud.get_accounts_by_user_id(session['user_id'])

    return render_template("profile.html", accounts=accounts)


@app.route("/create_account", methods=["POST"])
def create_account():
    """Create an account."""

    account_type = request.form.get("account_type")
    account_nickname = request.form.get("account_nickname")

    crud.create_account(user_id = session['user_id'],
                         account_type = account_type,
                         account_nickname = account_nickname)

    return redirect("/profile")


@app.route("/handle_account_removal")
def remove_account():
    """Remove an account."""

    account_id = request.args.get("account_id")

    print(f'Account_id is {account_id}')

    crud.remove_account_by_account_id(account_id)

    return redirect("/profile")


@app.route("/profile/<account_id>")
def show_budget(account_id):
    """Show projected budget for a particular account."""
      
    account = crud.get_account_by_account_id(account_id)
    if account == None or session['user_id'] != account.user_id:
        flash("Access denied!!!")
        return redirect('/profile')
   
    list_of_recurrent_entries = crud.retrieve_recurrent_entries_by_account_id(account_id)
    all_recurrent_entries_list = crud.list_of_recurrent_entries_with_all_dates(list_of_recurrent_entries)
    
    single_entries = crud.sort_entry_logs(account_id)
    complete_list = single_entries + all_recurrent_entries_list

    def sortfxn(entry):
        return entry.date
    
    complete_list.sort(key=sortfxn)

    return render_template("account_details.html",
                            account = account,
                            entries = complete_list)


@app.route("/create_transaction", methods=["POST"])
def create_transaction():
    """User to create transactions in account_details.html."""

    account_id = request.form.get('account_id')
    date = request.form.get("date")
    category = request.form.get("category")
    description = request.form.get("description")
    amount = request.form.get("amount")
    stop_date = request.form.get("stop_date")
    if stop_date == "":
        stop_date = date
    frequency_int = int(request.form.get("frequency_int"))
    frequency_unit = request.form.get("frequency_unit")
    frequency = crud.convert_frequency_to_num_of_day(frequency_int, frequency_unit)
    if frequency_int == 0:
        frequency = None

    crud.create_entry_log(account_id, 
                          date, 
                          category, 
                          description, 
                          amount,
                          stop_date,
                          frequency)
  
    return redirect(f"/profile/{account_id}")
   

@app.route("/handle_entry_removal")
def remove_entry():
    """Remove an entry."""

    entry_id = request.args.get('entry_id')
    account_id = request.args.get('account_id')

    print(f'entry_id is {entry_id}')
    print(f'account_id is {account_id}')

    crud.remove_entry_by_entry_id(entry_id)

    return redirect(f"/profile/{account_id}")


@app.route("/logout")
def process_logout():

    session.pop("user_name", None)
    session.pop("user_id", None)
    flash("You are logged out.")
    print(f"SESSION SHOULD BE RESEST TO {session}")

    return redirect("/")


@app.errorhandler(404)
def not_found(error):
    return "Oops. You got to the 404 page..."


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")