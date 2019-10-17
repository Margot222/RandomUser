import requests
import re
from random import randint
from .models import User


def get_five_more_users(num_users=5):
    count = 0
    while count != num_users:
        response = requests.get('https://randomuser.me/api/?inc=gender,name,location,email')
        user_data = response.json()['results'][0]
        f_name = user_data['name']['first']
        l_name = user_data['name']['last']
        r_inside = re.compile(r'[r,R]')
        new_user = User()
        if not r_inside.findall(f_name + l_name):
            new_user.save_user(user_data['gender'], f_name, l_name, user_data['location'], user_data['email'])
            count += 1


def get_one_random_user_from_db():
    users = User.objects.all()
    if not users.exists():
        get_five_more_users()
    count = users.count()
    rand_ind = randint(0, count - 1)
    return users[rand_ind]

