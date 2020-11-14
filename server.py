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

    email = request.form["email"]
    password = request.form["password"]
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

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form["email"]
    password = request.form["password"]

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
    """Show user profile."""

    accounts = crud.get_accounts_by_user_id(session['user_id'])

    return render_template("profile.html", accounts=accounts)


@app.route("/create_account", methods=["POST"])
def create_account():
    """Create an account."""

    account_type = request.form["account_type"]
    account_nickname = request.form["account_nickname"]

    crud.create_account(user_id = session['user_id'],
                         account_type = account_type,
                         account_nickname = account_nickname)

    return redirect("/profile")


@app.route("/profile/<account_id>")
def show_budget(account_id):
    """Show projected budget for a particular account."""

    account = crud.get_account_by_account_id(account_id)
    sort_entries = crud.sort_entry_logs(account_id)


    return render_template("account_details.html",
                            account = account,
                            entries = sort_entries)


@app.route("/create_transaction", methods=["POST"])
def create_transaction():
    """User to create transactions in account_details.html."""

    account_id = request.form['account_id']
    date = request.form["date"]
    category = request.form["category"]
    description = request.form["description"]
    amount = request.form["amount"]

    crud.create_entry_log(account_id, 
                          date, 
                          category, 
                          description, 
                          amount)

    print(request.form['account_id'])

    return redirect(f"/profile/{account_id}")
    

@app.route("/logout")
def process_logout():

    session.pop("user_name", None)
    session.pop("user_id", None)
    print(f"SESSION SHOULD BE RESEST TO {session}")

    return redirect("/")


@app.errorhandler(404)
def not_found(error):
    return "Oops. You got to the 404 page..."


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="0.0.0.0")