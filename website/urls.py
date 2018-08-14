"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index-view'),
    path('services/', views.service_view, name='service-view'),
    path('features/', views.features_view, name='feature-view'),
    path('pricing/', views.pricing_view, name='price-view'),
    path('contact/', views.contact_view, name='contact-view'),
    path('blog/', views.blog_view, name='blog-view'),
    path('about/', views.about_view, name='about-view'),
]

urlpatterns += [
	path('send-view-visit/', views.send_view_visit, name='send-view-visit')
]