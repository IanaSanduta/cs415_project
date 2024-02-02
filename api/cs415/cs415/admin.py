from django.contrib import admin
from .models import Expenses, Savings, User

admin.site.register(Expenses)
admin.site.register(Savings)
admin.site.register(User)
