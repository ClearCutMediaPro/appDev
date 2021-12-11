from django.db import models
from sorl.thumbnail import ImageField

# Create your models here.
class Testimonial(models.Model):
    date = models.DateField(auto_now='auto')
    name = models.CharField(max_length=50, blank=False, null=False)
    quote = models.TextField(max_length=550, blank=False, null=False)
    image = models.ImageField( )
    
    def  __str__(self) -> str: # this command ensure that the title is displayed correctly in the backend
        return self.name[0:50]