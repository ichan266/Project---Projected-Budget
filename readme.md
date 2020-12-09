![alt text][logo]

[logo]: static/ThistleLogo.png

Thistle is a web application that provides users a better tool to keep track of their income and expenses. It allows them to see a 12-month financial picture, empowering them to make better financial plans and decisions.

## Contents

* [Features](#features)
* [Tech Stack](#tech-stack)
* [Installation](#installation)
* [About the Author](#about-author)

## <a name="features"></a>Features

### Homepage
Users can log in or sign up here.
![Thistle Homepage](/static/homepage.png)

### Profile
After logging in, it will take users to their profile page. User can:

* See their list of accounts
* Add new accounts with description
* Remove an account
* Click on an account will take them to the next page, account details

**Profile Page**
![Profile Page](/static/profile_page.png)

### Account Details

See a list of entries, sorted by date
Recurrent entry* with the same entry ID highlighted in the same color. Negative balances are highlighted in red
![Highlight recurrent entry](/static/recurrent_entry_highlight.gif)
*Recurrent entry is an entry with specific time interval, such as every 2 weeks, with a stop date specified by the user. In account details, any recurrent entries will be calculated for a one-year interval from the time of login.

**Edit amount inline**
![Edit amount](/static/edit_amount.gif)

**Add one-time or recurrent entry using this form**
![Create new entry](/static/create_new_transaction.png)

## <a name="tech-stack"></a>Tech Stack

**Backend/framework** | Python, Flask, Flask_SQLAlchemy, Jinja

**Frontend** | JavaScript, jQuery, Bootstrap, CSS, HTML

**Database** | PostgreSQL

**Testing** | Python unittest, coverage

## <a name="installation"></a>Installation

This project was developed in a virtual environment using [VirturalBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html)

Other Sysytem requirements include:

* [Python3](https://www.python.org/downloads/) - Server
* [PostgreSQL](https://www.postgresql.org/download/) - Database

Once system requirements above are met, please follow the following steps:

1. Clone this repo
```
$ git clone https://github.com/ichan266/Project---Projected-Budget.git
```

2. Create and activate a virtual environment
```
$ virtualenv env
$ source env/bin/activate
```

3. Install dependencies
```
$ pip3 install -r requirements.txt
```

4. Seed database: this repo comes with seed_database.py. Simply run this command in the terminal
```
$ python3 seed_database.py
```

5. Start the server
```
$ python3 server.py
```

6. Go to localhost:5000 in your browser. The website should be up and running! :wink:

## <a name="about-author"></a>About the Author

Iris was a pharmacist before enrolling in [Hackbright Software Engineering](https://hackbrightacademy.com/) Boot Camp. She always likes to find different ways to help improve efficiency. She wholeheartedly believes that technology together with software can help us achieve that, and more.

For her capstone project at Hackbright, she created this website to enable users to see their projected budget for the next 12 months. By providing a clearer picture, she believes it can empower users to better foresee their financial future.