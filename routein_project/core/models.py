from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields if needed, like profile picture, bio, etc. in the future

    def __str__(self):
        return self.user.username