from django.db import models

from users.models import User

# Create your models here.


class Mall(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )
