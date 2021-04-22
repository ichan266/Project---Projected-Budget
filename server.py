from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for, jsonify)
from jinja2 import StrictUndefined
# import datetime
import os
import sys

from model import connect_to_db, db
import crud

#! In order to use the secret key, I need to type in "source secrets.sh"
#! in the terminal before starting the server

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.jinja_env.undefined = StrictUndefined
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/api/login", methods=["POST"])
def login():
    """ Confirm account and take user to welcome page."""

    data = request.get_json()  # * request.get_json() is a built-in flask object
    print("I GOT SOME DATA")
    print(data)
    email = data["email"]
    print(f"email is {email}")
    password = data["password"]
    print(f"password is {password}")
    user = crud.get_user_by_email(email)

    if user == None or not user.check_password(password):
        return jsonify("Email and password did not match our records. Please try again.", "danger")
    else:
        return jsonify("Successful")

    # valid_user = True  # Using crud to confirm user
    # if valid_user:
    #     return jsonify("banana bunny muffins")
    # else:
    #     return jsonify("login failed")

@app.route("/api/create_user", methods=["POST"])
def register_user():
    """Create a new user."""

    newData = request.get_json()
    first_name = newData["firstName"]
    last_name = newData["lastName"]
    new_email = newData["newEmail"]
    new_password = newData["newPassword"]
    new_password_conf = newData["new_password_conf"]

    if crud.get_user_by_email(new_email) != None:
        flash("Account already exists. Please try again.", "danger")
    elif new_password == new_password_conf:
        user = crud.create_user(first_name, last_name, new_email, new_password)
        # session['user_name'] = f"{user.first_name} {user.last_name}"
        # session['user_id'] = user.user_id
        # flash("Account Created!", "success")
        # return redirect("/profile")
        return jsonify("Hi {user.first_name}")
    else:
        flash("Passwords do not match. Please try again.", "danger")

    return redirect("/")


@app.route("/login")
@app.route("/about")
@app.route("/search")
@app.route("/")
def root():
    """Render homepage."""

    return render_template("root.html")


local = "-local" in sys.argv
connect_to_db(app, local=local)

if __name__ == "__main__":
    if local:
        app.run(debug=True, host="0.0.0.0")
    else:
        app.run()

# @ 6 valid data types for JSON
# @ strings
# @ arrays
# @ object
# @ numbers
# @ boolean
# @ null
#! It won't be able to take SQLAlchemy objects!!!
