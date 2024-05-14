from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
#define our model as an object and post is the name of the object
##models.model means the Post ia a django model and it should be saved in the database
class Post(models.Model):
#define the properties
##ForeignKey is a link to another model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# define publish method
    def publish(self):
        self.published_date = timezone.now()
        self.save()

#return the text string with a post title
    def __str__(self):
        return self.title
    
##put our methods inside a class rem OOP
