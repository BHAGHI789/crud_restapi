from django.db import models

# Create your models here.
class BookModel(models.Model):
    name=models.CharField(max_length=10)
    author=models.CharField(max_length=100)
    read_by=models.CharField(max_length=100)

    def __str__(self):
        return self.name