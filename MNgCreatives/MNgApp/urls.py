from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('portfolio/', views.portfolio_details, name = 'portfolio'),
    path('starter/', views.starter_page, name = 'starter'),
    path('services/', views.services, name = 'services'),
    path('about/', views.about, name = 'about'),
    path('resume/', views.resume, name = 'resume'),
]