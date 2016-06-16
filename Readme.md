**Upwork test.**

## Features

* Upload samples(A\B) with drag-n-drop
* For SampleB, calculates the sum of the column "Savings" for each category in the column "Dryden Category", and saves that information in a postgres database
* For SampleA, calculates the sum of "Total Purchase Dollars" for each category in the column "Class", and saves that information in a postgres database
* Admin pages



## Quick start:

1. `$ git clone git@github.com:ToGoBananas/upwork_test.git`
2. `$ git cd upwork_test`
3. `$ virtualenv venv --python=python2.7`
4. `$ source venv/bin/activate`
5. `$ pip install -r requirements.txt`
6. Log into psql console and create database and `$ create database upwork_test with owner postgres`
7. In directory with manage.py and activated envirnoment `$ python manage.py migrate`
8. create superuser `$ python manage.py createsuperuser`
9. `$ python manage.py runserver`


Site available at: ttp://127.0.0.1:8000/

Admin page: ttp://127.0.0.1:8000/admin/