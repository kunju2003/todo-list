from django.db import models

# Create your models here.
class todotable(models.Model):
    sub=models.TextField()
    date=models.DateField(auto_now_add=True,null=True)