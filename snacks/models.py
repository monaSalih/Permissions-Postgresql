from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Snack(models.Model):
    purchaser  =  models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description  = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    #type time stamp and use add to add time and date when create thing
    updated_at = models.DateTimeField(auto_now= True)
    #type time stamp and use add to add time and date when update thing



    def __str__(self):
        return self.title