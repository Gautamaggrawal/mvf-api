import uuid

from django.db import models


class Account(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    balance = models.FloatField()

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    def __str__(self):
        return str(self.id)
