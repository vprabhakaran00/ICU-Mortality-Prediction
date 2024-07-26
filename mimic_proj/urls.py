"""
URL configuration for mimic_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# This is the main URL configuration file for this Django project.

# This file defines the URL patterns for the entire project and includes URLs from
# different apps using the include function.

from django.contrib import admin    # admin is responsible for Django's built-in admin interface

# path define individual URL patterns
# 'include' includes URL patterns from other apps
from django.urls import include, path


# define url pattern for this project
urlpatterns = [
    # include urls from 'results' app in base url website.com/
    path('', include('result.urls')),

    # maps pattern 'admin/' to the Django admin interface
    # website.com/admin directs user to admin interface, manage app data
    path('admin/', admin.site.urls),
]
