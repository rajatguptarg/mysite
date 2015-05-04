from django.db import models
from django.contrib import admin


class BlogPost(models.Model):
    """
    Model Structure of Blog in DB
    """
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        """
        Ordering according to timestamp
         """
        ordering = ('-timestamp',)

    """
    def __init__(self, title, body, timestamp):
        self.title = title
        self.body = body
        self.timestamp = timestamp
    """


class BlogPostAdmin(admin.ModelAdmin):
    """
    Model for admin
    """
    list_display = ('title', 'timestamp')

admin.site.register(BlogPost, BlogPostAdmin)
