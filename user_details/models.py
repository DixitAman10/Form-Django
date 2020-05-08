from django.db import models
from django.core.validators import RegexValidator


TITLE_CHOICES = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Ms', 'Ms')
)


class UserDetails(models.Model):

    title = models.CharField(max_length=3, choices=TITLE_CHOICES, blank=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '0123456789'. Up to 10 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    address = models.TextField()
