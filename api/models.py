from django.db import models

# Create your models here.


class Random_UUID(models.Model):
    uuid = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """one-line docstring for representing the L object."""
        return self.uuid
