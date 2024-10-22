'''Models for the post application'''
from django.db import models


class Post(models.Model):
    '''Model for a post'''
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
                               null=True, blank=True)


class Author(models.Model):
    '''Define and display the author'''
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
