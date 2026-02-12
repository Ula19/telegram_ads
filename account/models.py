from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Пока оставляем пустым, username и password уже включены в AbstractUser
    pass


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return f"Профиль {self.user.username}"


class AccountNumber(models.Model):
    phone_number = models.ForeignKey(Profile, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    title = models.CharField()
