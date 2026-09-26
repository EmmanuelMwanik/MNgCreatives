from django.urls import path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    ...
]


urlpatterns = [
    path('', views.index, name = 'index'),
    path('portfolio/', views.portfolio_details, name = 'portfolio'),
    path('starter/', views.starter_page, name = 'starter'),
    path('services/', views.services, name = 'services'),
    path('about/', views.about, name = 'about'),
    path('resume/', views.resume, name = 'resume'),
    path('contact/', views.contact, name = 'contact'),
    path('testimonials/', views.testimonials, name = 'testimonials'),
    path(
    'sitemap.xml',
    sitemap,
    {'sitemaps': sitemaps},
    name='django.contrib.sitemaps.views.sitemap',
),
]