from django.db import models
from project.settings import AUT


class Blog(models.Model):
    title = models.CharField(max_length=255) 
    content = models.TextField()
    like_count = models.IntegerField(default=0)
    link = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField()

    def __str__(self):
        return self.title
    
    def delete(self):
        self.title = ""
        self.content = "delete post"
        self.author = None
        self.save()

class Comment(models.Model):
    text = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models., null=True)
    # see about many to many field