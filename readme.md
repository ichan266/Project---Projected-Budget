![alt text][logo]

[logo]: static/ThistleLogo.png

Thistle is a web application that provides users a better tool to keep track of their income and expenses. It allows them to see a 12-month financial picture, empowering them to make better financial plans and decisions.

## Tech Stack

**Languages** | Python, JavaScript (AJAX), HTML, CSS

**Frameworks & Libraries** | Flask, Flask_SQLAlchemy, jQuery, Bootstrap, Jinja, datetime

**Database** | PostgreSQL

**Testing** | Python unittest, coverage

## Features

### Homepage
Users can log in or sign up here.
![Thistle Homepage](/static/homepage.png)


### Profile
After logging in, it will take users to their profile page. User can:

* See their list of accounts
* Add new accounts with description
* Remove an account
* Click on an account will take them to the next page, account details

![Profile Page](/static/profile_page.png)

### Account Details

* See a list of entries, sorted by date
* Recurrent entry* with the same entry ID highlighted in the same color. Negative balances are highlighted in red
![Highlight recurrent entry](/static/recurrent_entry_highlight.gif)

* Edit amount inline
![Edit amount](/static/edit_amount.gif)

* Add one-time or recurrent entry using this form
![Create new entry](/static/create_new_transaction.png)

*Recurrent entry is an entry with specific time interval, such as every 2 weeks, with a stop date specified by the user. In account details, any recurrent entries will be calculated for a one-year interval from the time of login.
