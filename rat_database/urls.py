from django.conf.urls import url

from . import views

app_name='rat_database'
urlpatterns= [
    url(r'^rat_database/$', views.home, name='home'),

]