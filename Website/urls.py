from django.conf.urls import url

from . import views

app_name = 'Website'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^lab_info/$', views.lab_info, name='lab_info'),
    url(r'^lab_members/$', views.lab_members, name='lab_members'),
    url(r'^lab_publications/$', views.lab_publications, name='lab_publications'),
    url(r'^contact_form/$', views.contact_form, name='contact_form'),
]
