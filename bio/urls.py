from django.conf.urls import url
from . import views

app_name = 'bio'
urlpatterns = [

    url(r'^$', views.about, name='about'),
]