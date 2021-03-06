"""ingredient_order_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.shortcuts import redirect
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', lambda request: redirect('foodprod:index', permanent=False)),
    path('', include(('registration.urls', 'registration'), namespace='registration')),
    path('admin/', admin.site.urls),
    path('foodprod/', include(('foodprod.urls', 'foodprod'), namespace='foodprod')),
    path('notes/', include(('notes.urls', 'notes'), namespace='notes')),
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += staticfiles_urlpatterns()
