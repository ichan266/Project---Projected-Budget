from flask import (Flask, render_template, request, flash, session,
                   redirect, url_for, jsonify)
# from jinja2 import StrictUndefined
# import datetime
import os
import sys

# from model import connect_to_db, db
# import crud

#! In order to use the secret key, I need to type in "source secrets.sh"
#! in the terminal before starting the server

app = Flask(__name__)
# app.secret_key = os.environ["SECRET_KEY"]
# app.jinja_env.undefined = StrictUndefined
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()  # * request.get_json() is a built-in flask object
    print('I GOT SOME DATA!')
    print(data)
    email = data["email"]
    password = data["password"]

    valid_user = True  # Using crud to confirm user
    if valid_user:
        return jsonify("banana bunny muffins")
    else:
        return jsonify("login failed")


@app.route("/login")
@app.route("/about")
@app.route("/search")
@app.route("/")
def root():
    """Render homepage."""

    return render_template("root.html")


local = "-local" in sys.argv
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
