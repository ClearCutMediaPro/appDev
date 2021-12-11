from django.urls import path
from . import views
from feed.views import HomePageView


app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    
]