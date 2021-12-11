from typing import Text
from django.db import models
from django.views.generic import TemplateView

from .models import Testimonial

from django.contrib import messages # import messages from django.contrib


class TestimonialPageView(TemplateView):
    http_method_names = ['get']
    template_name = 'home.html'
    model = Testimonial
    context_object_name = 'testimonials'  
    queryset = Testimonial.objects.all().order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all().order_by('-id')[0:3] # Django get all of the posts and order them by their id descending
        return context