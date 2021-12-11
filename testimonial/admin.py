from django.contrib import admin

from .models import Testimonial

class PostTestimonial(admin.ModelAdmin):
    pass

admin.site.register(Testimonial, PostTestimonial)