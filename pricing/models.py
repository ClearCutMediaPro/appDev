from django.db import models

class Post (models.Model):
    service_choices = [
        ('Web Design'),
        ('Video Production'),
        ('Graphics Design'),
        ('Animation'),
    ]
    
    service = models.CharField(max_length=50, choices=service_choices)
    price = models.IntegerField()
    contents = models.BooleanField()
    
    
    pass
