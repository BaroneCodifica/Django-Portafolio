from django.db import models
import datetime

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/images', blank=True, null=True)
    date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.title
