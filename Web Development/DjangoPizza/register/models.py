from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):

    # user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    confirmed = models.BooleanField('Confirmed", default=False')
    first_name = models.CharField("First Name",max_length=50, blank=True)
    last_name = models.CharField("Last Name", max_length=50, blank=True)
    address = models.CharField("Address", max_length=100, blank=True)
    city = models.CharField("City", max_length=50, blank=True)
    state = models.CharField("State", max_length=50, blank=True)
    zip_code = models.CharField("Zip Code", max_length=5, blank=True)




# def __str__(self):
#     return f'{self.user.username} Profile'
#
# def save(self, *args, **kwargs):
#     super().save(*args, **kwargs)
