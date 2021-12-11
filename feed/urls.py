from django.urls import path
from . import views
from .views import feedPageView, feedDetailView


app_name = 'feed'

urlpatterns = [
    path('', views.feedPageView.as_view(), name='index'),
    path('detail/<int:pk>/', views.feedDetailView.as_view(), name='detail')
    
]