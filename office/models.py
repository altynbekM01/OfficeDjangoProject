from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(models.Model):

    name = models.CharField(max_length=15, db_index=True)
    surname = models.CharField(max_length=15, db_index=True)
    middleName = models.CharField(max_length=15, db_index=True)
    position = models.CharField(max_length=15, db_index=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(max_digits=7, decimal_places=3)
    chief = models.CharField(max_length=50, db_index=True)


    objects = models.Manager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name

class User(AbstractUser):
    pass

