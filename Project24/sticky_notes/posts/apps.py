'''App configuration for the posts application.'''
from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''Configuration for the posts application.'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
