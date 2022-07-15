from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    BLACK = 'BK'
    BLUE = 'BL'
    RED = 'RED'
    GREEN = 'GR'
    USER_COLOR_CHOICES = [
        (BLACK, 'BLACK')
    ]
    balance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True
    )
    login_color = models.CharField(
        max_length=10,
        choices=USER_COLOR_CHOICES,
        default=BLACK,
    )
    background_color = models.CharField(
        max_length=10,
        choices=USER_COLOR_CHOICES,
        default=BLACK,
    )
