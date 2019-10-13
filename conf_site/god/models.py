from django.db import models

# Create your models here.


class confDB(models.Model):
    imageURL = models.URLField(max_length=500)
    confEndDate = models.CharField(max_length=120)
    confStartDate = models.CharField(max_length=120)
    confName = models.CharField(max_length=200)
    venue = models.TextField()
    confUrl = models.URLField(max_length=200)

    def __str__(self):
        return self.confName
