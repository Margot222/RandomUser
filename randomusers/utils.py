import requests
import re
import sys
from random import randint
from .models import User


def get_five_more_users(num_users=5):
    count = 0
    max_iterations = 100
    added_users = []
    while count != num_users and max_iterations >= 0:
        max_iterations -= 1
        try:
            response = requests.get('https://randomuser.me/api/?inc=gender,name,location,email,picture')
        except requests.exceptions.RequestException:
            return ["An error occurred, please try again"]
        user_data = response.json()['results'][0]
        f_name = user_data['name']['first']
        l_name = user_data['name']['last']
        r_inside = re.compile(r'[r,R]')
        new_user = User()
        if not r_inside.findall(f_name + l_name):
            location = str(user_data['location']['street']['number']) + ', ' \
                       + user_data['location']['street']['name'] \
                       + ', ' + user_data['location']['city'] + ', ' + user_data['location']['country']
            new_user.save_user(user_data['gender'], f_name, l_name, location,
                               user_data['email'], user_data['picture']['large'])
            added_users.append(new_user)
            count += 1
    return added_users


def get_one_random_user_from_db():
    users = User.objects.all()
    if not users.exists():
        get_five_more_users()
    count = users.count()
    rand_ind = randint(0, count - 1)
    return users[rand_ind]


def get_all_users_from_db():
    users = User.objects.all()
    return users


def delete_all_users_from_db():
    users = User.objects.all().delete()
    return users
