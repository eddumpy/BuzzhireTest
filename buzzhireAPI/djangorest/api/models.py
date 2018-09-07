from django.db import models

# Create your models here.
class Event(models.Model):
    start = models.DateTimeField(auto_now_add=False)
    end = models.DateTimeField(auto_now_add=False)
    label = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.label
