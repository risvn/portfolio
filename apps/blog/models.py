from django.db import models




class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date_posted = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-date_posted"]

    def __str__(self):
        return self.title



