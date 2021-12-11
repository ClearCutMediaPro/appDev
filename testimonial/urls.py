from django.urls import path
from . import views
from testimonial.views import TestimonialPageView


app_name = 'testimonial'

urlpatterns = [
    path('', TestimonialPageView.as_view(), name='testimonial'),
    
]