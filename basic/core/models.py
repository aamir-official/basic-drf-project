from django.db import models

# Create your models here.


class MyUser(models.Model):
    name = models.CharField(max_length=64)
    user = models.ForeignKey('auth.User')

    def __str__(self):
        return "%s (%s)" % (self.name, self.user)
