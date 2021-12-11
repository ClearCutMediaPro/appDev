from django.urls import path
from . import views
from testimonial.views import TestimonialPageView


app_name = 'testimonial'

urlpatterns = [
    path('', views.TestimonialPageView.as_view(), name='testimonial'),
    
]