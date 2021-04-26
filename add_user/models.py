from django.db import models


class AddUser(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
