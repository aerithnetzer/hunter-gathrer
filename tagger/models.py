from typing import final
from django.db import models


class Occupation(models.Model):
    id = models.CharField(max_length=8)


class Office(models.Model):
    id = models.CharField(max_length=8)


class Status(models.Model):
    id = models.CharField(max_length=8)


class Residence(models.Model):
    id = models.CharField(max_length=8)


class WorkLocation(models.Model):
    id = models.CharField(max_length=8)


class Person(models.Model):
    SEX_CHOICES = {"M": "Male", "F": "Female", "X": "Unknown"}
    SUBSCRIPTION_CHOICES = {"S": "Signature", "M": "Mark", "X": None}
    id: models.CharField = models.CharField(max_length=8)
    headword: models.CharField = models.CharField(max_length=256)  # Display name?
    surname: models.CharField = models.CharField(max_length=50)
    form: models.CharField = models.CharField(max_length=120)
    qualifier: models.CharField = models.CharField(max_length=80)
    alias: models.CharField = models.CharField(max_length=80)
    sex: models.CharField = models.CharField(
        max_length=2, choices=SEX_CHOICES, default="X"
    )
    imputed_birth_year: models.DateField = models.DateField()
    occupation: models.ForeignKey = models.ForeignKey(
        Occupation, on_delete=models.CASCADE
    )
    office: models.ForeignKey = models.ForeignKey(Office, on_delete=models.CASCADE)
    status: models.ForeignKey = models.ForeignKey(Status, on_delete=models.CASCADE)
    residence: models.ForeignKey = models.ForeignKey(
        Residence, on_delete=models.CASCADE
    )
    work_location: models.ForeignKey = models.ForeignKey(
        WorkLocation, on_delete=models.CASCADE
    )
    notes: models.TextField = models.TextField()
    subscription: models.CharField = models.CharField(max_length=1, nullable=True)
