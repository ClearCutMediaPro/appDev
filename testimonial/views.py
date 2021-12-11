from typing import Text
from django.views.generic import ListView

from .models import Testimonial

from django.contrib import messages # import messages from django.contrib


class TestimonialPageView(ListView):
    http_method_names = ['get']
    template_name = 'testimonial.html'
    model = Testimonial
    context_object_name = 'testimonials'  
    queryset = Testimonial.objects.all().order_by('-id')[0:1]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all().order_by('-id') # Django get all of the posts and order them by their id descending
        return context