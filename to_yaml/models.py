from django.db import models


class Attributes(models.Model):
    info = models.CharField(max_length=200)


class Elements(models.Model):
    name = models.CharField(max_length=200)


class TypeAttribute(models.Model):
    element_id = models.IntegerField()
    attribute_id = models.IntegerField()


class Recording(models.Model):
    test_case = models.CharField(max_length=200)
    executor = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
