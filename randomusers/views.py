from django.shortcuts import render
from .utils import get_one_random_user_from_db, get_five_more_users, get_all_users_from_db, delete_all_users_from_db


def random_user(request):
    user = get_one_random_user_from_db()
    return render(request, 'randomusers/random_user.html', {'f_name': user.first_name, 'l_name': user.last_name,
                                                            'gender': user.gender, 'location': user.location,
                                                            'email': user.email, 'pic': user.pic})


def five_new_users(request):
    five_users = get_five_more_users()
    return render(request, 'randomusers/five_new_users.html', {'users': five_users})


def all_users(request):
    all_users = get_all_users_from_db()
    return render(request, 'randomusers/all_users.html', {'users': all_users})


def users_deleted(request):
    delete_all_users_from_db()
    return render(request, 'randomusers/users_deleted.html')
