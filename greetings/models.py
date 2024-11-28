from django.db import models

class User(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
