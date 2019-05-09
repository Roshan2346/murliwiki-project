from django.db import models


class Results(models.Model):
    date = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    month = models.CharField(max_length=22)
    year = models.IntegerField()
    file = models.FileField(upload_to='file/')

    def __str__(self):
        return self.date
