from django.contrib import admin
from .models import User, Expense, TotalAmount
# Register your models here.

admin.site.register(User)
admin.site.register(Expense)
admin.site.register(TotalAmount)