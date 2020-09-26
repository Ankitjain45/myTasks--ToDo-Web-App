from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title     