"""
URL configuration for Auction_Site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',  TemplateView.as_view(template_name='main_menu.html'), name='main_menu'),

    path('profile/',  include('login_app.urls')),

    path('About_Us/', TemplateView.as_view(template_name='info/About_Us.html'), name='About_Us'),
    path('Projects/', TemplateView.as_view(template_name='info/Projects.html'), name='Projects'),
    path('Terms_of_use/', TemplateView.as_view(template_name='info/Terms_of_use.html'), name='Terms_of_use'),
]
