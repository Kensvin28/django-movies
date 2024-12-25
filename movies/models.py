from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    imgPath = models.CharField(max_length=200)
    duration = models.IntegerField() # in minutes
    genre = models.JSONField() # genre as JSON array
    language = models.CharField(max_length=50)
    mpaaRating = models.JSONField() # rating as JSON object
    userRating = models.CharField(max_length=5)

    def __str__(self):
        return self.name
