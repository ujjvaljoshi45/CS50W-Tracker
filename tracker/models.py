from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def serialize(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'date': self.date,
            'description': self.description,
            'name': self.name,
        }

class TotalAmount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    totalAmount = models.DecimalField(max_digits=10, decimal_places=2)
