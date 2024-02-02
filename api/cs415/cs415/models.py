from django.db import models

class Expenses(models.Model):
    expenses_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Expenses'
    
    def __str__(self):
        return f'{self.amount} {self.date} {self.description}'


class Savings(models.Model):
    savings_id = models.AutoField(primary_key=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Savings'
    
    def __str__(self):
        return f'{self.amount} {self.date} {self.description}'


class User(models.Model):
    username_id = models.AutoField(primary_key=True)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'User'
    
    def __str__(self):
        return f'{self.username}'