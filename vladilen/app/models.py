from django.db import models

class List(models.Model):
    title=models.CharField(max_length=155)
    def __str__(self):
        return self.title
