from django.db import models

# Create your models here.
class Data(models.Model):
    upload = models.FileField()

    def __str__(self):
        return str(self.pk)