from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=60)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.name
