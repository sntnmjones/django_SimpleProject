# pages/urls.py

from django.urls import path
from . import views

# as_view() used with class-based views.
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]