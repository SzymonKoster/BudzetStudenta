from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
'''
class AccountInfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_budget = models.IntegerField()
    
    def __str__(self):
        return self.username
'''
class ExpenseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=20)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)

class EntertainmentInfo(models.Model):
    id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=20)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)

class StudyInfo(models.Model):
    id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=20)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)

class TravelsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=20)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)

class SavingsInfo(models.Model):
    id = models.AutoField(primary_key=True)
    expense_name = models.CharField(max_length=20)
    cost = models.FloatField()
    date_added = models.DateField()
    user_expense = models.ForeignKey(User, on_delete=models.CASCADE)