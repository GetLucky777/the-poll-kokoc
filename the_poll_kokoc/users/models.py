from django.db import models
from django.contrib.auth.models import AbstractUser


class Colors(models.Model):
    BLACK = 'BLACK'
    BLUE = 'BLUE'
    RED = 'RED'
    GREEN = 'GREEN'
    USER_COLOR_CHOICES = [
        (BLACK, 'BLACK'),
        (BLUE, 'BLUE'),
        (RED, 'RED'),
        (GREEN, 'GREEN')
    ]

    color = models.CharField(
        max_length=10,
        choices=USER_COLOR_CHOICES
    )
    cost = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    def __str__(self):
        return self.color


class User(AbstractUser):
    balance = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0.00
    )
    login_color = models.ForeignKey(
        Colors,
        on_delete=models.CASCADE,
        related_name='users_login_color',
        null=True
    )
    background_color = models.ForeignKey(
        Colors,
        on_delete=models.CASCADE,
        related_name='users_backgrnd_color',
        null=True
    )

