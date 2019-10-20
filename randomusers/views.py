from django.shortcuts import render
from .utils import get_one_random_user_from_db


def random_user(request):
    user = get_one_random_user_from_db()
    return render(request, 'randomusers/random_user.html', {'f_name': user.first_name, 'l_name': user.last_name,
                                                            'gender': user.gender, 'location': user.location,
                                                            'email': user.email, 'pic': user.pic})
