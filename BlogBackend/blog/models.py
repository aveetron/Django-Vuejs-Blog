from django.db import models

# Create your models here.


# Blog model decribing it's properties
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
