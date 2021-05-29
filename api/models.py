from django.db import models

# Create your models here.


class Random_UUID(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    uuid = models.CharField(max_length=250)
