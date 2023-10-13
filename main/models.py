from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=(('Cold', 'Cold'), ('Hot', 'Hot')))
    sweetness = models.CharField(max_length=50, choices=(('Less Sweet', 'Less Sweet'), ('Normal Sweet', 'Normal Sweet')))
    is_deleted = models.BooleanField(default=False)