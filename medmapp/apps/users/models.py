from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.
class User(AbstractUser):

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    # Default values for USERNAME_FIELD and REQUIRED_FIELDS
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {"refresh": str(refresh), "access": str(refresh.access_token)}

    def __str__(self):
        return str(self.username)