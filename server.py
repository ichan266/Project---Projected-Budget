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


# @app.route('/users', methods=['POST'])
# def register_user():
#     """Create a new user."""

#     email = request.form.get('email')
#     password = request.form.get('password')

#     user = crud.get_user_by_email(email)
#     if user:
#         flash('Cannot create an account with that email. Try again.')
#     else:
#         crud.create_user(email, password)
#         flash('Account created! Please log in.')
#         # render_template()  # Need to write a page to take user to a page to add first name and last name

#     return redirect('/')


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
        print(f"THE SESSION IS {session['user_name']}")
        return render_template('welcome.html')

    return redirect('/')



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')