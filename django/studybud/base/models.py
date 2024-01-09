from django.db import models

# Create your models here.

# model -> table are synonymous 
class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # participants = 
    updated = models.DateTimeField(auto_now=True) # take timestamp every time updated 
    created = models.DateTimeField(auto_now_add=True) # only when created instance

    def __str__(self):
        return self.name 