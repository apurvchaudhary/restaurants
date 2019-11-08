# restaurants
demo project

step 1
first clone repo with command : git clone https://github.com/apurvchaudhary/restaurants.git

step 2
#Note: I created this project on python 3.7, earlier version would not support some of functionality.
creating virtual environment, install virtualenv if not installed for installation google it
for creating python3 virtualenv : python3 -m venv env_name

step 3
be in directory where venv located or set path as per your system for venv
activate env : source env_name/bin/activate

step 4
upgrade pip if required
install all dependency : pip install -r requirement.text (path for requirement.txt)

step 5
migrate data to db : python manage.py migrate

step 6
creating superuser for admin access : python manage.py createsuperuser
provide username, email and password, this will create a superuser i.e admin

step 7
run your app on local server : python manage.py runserver (it will run by default on 127.0.0.1:8000)

step 8
upload restaurant data from sheet : login admin with your user id and password on link http://127.0.0.1:8000/admin

step 9
upload : goto Data File table , select first restaurant_detail file from system then restaurant location file
click on save, this will load all data to tables

step 10
now play with data and web app
