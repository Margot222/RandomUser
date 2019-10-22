RandomUser uses https://randomuser.me/ API to fetch users, five at a time and with the condition that their firstname and lastname do not contain the letter "r" or "R".
The Web app was created using Django framework. The users are stored in an sqlite db. 
The functionality includes:
- Show one random user on the homepage
- Add five more users to the database (without the letter "r")
- Show all users in the database
- Delete all users from the database

The webapp is available at http://margot.pythonanywhere.com

To run it locally:
1) Download the repository
2) Make sure Virtualenv and Python are installed on your system
3) Run command "virtualanv venv" in your console
4) Activate the virtual environment by running "venv\Scripts\activate"
5) Install required packages by running "pip install -r requirements.txt" inside you virtual environment
6) Run command "python manage.py migrate" inside you virtual environment
7) Run command "python manage.py runserver" inside you virtual environment
8) The app should be available at "127.0.0.1:8000"
