from django.db import models
from acc.models import User

# Create your models here.

class Topic(models.Model):
    subject = models.CharField(max_length=100)
    maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="maker")
    content = models.TextField()
    voter = models.ManyToManyField(User, blank=True, related_name="voter")

    def __str__(self):
        return self.subject

class Choice(models.Model):
    top = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    comment = models.TextField()
    choicer = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.top}_{self.name}"