from django.conf import settings
from django.db import models


class User(models.Model):
    gender = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    location = models.TextField()
    email = models.EmailField()

    def save_user(self, gender, f_name, l_name, location, email):
        self.gender = gender
        self.first_name = f_name
        self.last_name = l_name
        self.location = location
        self.email = email
        self.save()

