from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255) 
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    link = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title