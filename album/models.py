from django.db import models
from acc.models import User
# Create your models here.

class Album(models.Model):
    maker = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    pic = models.ImageField()

    def getpic(self):
        if self.pic:
            return self.pic.url
            
        return "/media/noimage.png"