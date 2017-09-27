from django.db import models

class LoginDetails(models.Model):
    username = models.CharField(verbose_name='Username', max_length=30)
    password = models.CharField(verbose_name='Password', max_length=40)

    def __str__(self):
        return 'Username=' + self.username + ' '+'Password = ' + ' ' + self.password
