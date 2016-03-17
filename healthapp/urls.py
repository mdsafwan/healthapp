"""healthapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from login.views import sendsms, login_doctor, register, login_patient,\
    prescription, dashboard, panic, sendpanic, newsfeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sendsms/', sendsms),
    url(r'^login_doctor/', login_doctor),
    url(r'^login_patient/',login_patient),
    url(r'^register/', register),
    url(r'^prescription/', prescription),
    url(r'^dashboard/', dashboard),
    url(r'^panic/', panic),
    url(r'^sendpanic/', sendpanic),
    url(r'^newsfeed/', newsfeed),
]
