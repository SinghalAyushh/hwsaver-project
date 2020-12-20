from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Fav(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    first_name = models.TextField()
    last_name = models.TextField()
    favourites= models.TextField()

    def __str__(self):
        return self.user.username
