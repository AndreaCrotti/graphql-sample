from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Address(models.Model):
    city = models.CharField(max_length=10)
    postcode = models.CharField(max_length=10)


class Customer(User):
    address = models.ForeignKey(Address)


class Loan(models.Model):
    user = models.ForeignKey(Customer)
    quantity = models.IntegerField(default=100, help_text="How much was lent")
    timestamp = models.DateTimeField(default=timezone.now)
