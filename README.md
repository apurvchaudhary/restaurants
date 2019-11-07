# restaurants
demo project

step 1
first clone repo with command : git clone https://github.com/apurvchaudhary/restaurants.git

step 2
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
run youe app on local server : python manage.py runserver (it will run by default on port 8000)