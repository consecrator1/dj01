from django.db import models
from acc.models import User
# Create your models here.

class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site_name = models.CharField(max_length=100)
    site_url = models.TextField()
    site_con = models.TextField()
    impo = models.BooleanField(default=False)

    def __str__(self):
        return self.site_name