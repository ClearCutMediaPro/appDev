from django.db import models
from sorl.thumbnail import ImageField

class Post (models.Model):
    location_choices = [
        ('Auckland, New Zealand','AKL'),
        ( 'Wellington, New Zealand', 'WLG'),
        ('Christchurch, New Zealand', 'CHC'),
        ('Queenstown, New Zealand', 'QT'),
        ]
    
    location = models.CharField(max_length=50, choices=location_choices) 
    quote = models.CharField(max_length=240, blank=False, null=False)
    description = models.TextField() 
    image = ImageField() 
    
    def  __str__(self) -> str: # this command ensure that the title is displayed correctly in the backend
        return self.quote[0:100]