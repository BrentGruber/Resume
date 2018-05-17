from django.conf.urls import url
from . import views

app_name = 'bio'
urlpatterns = [

    url(r'^$', views.about, name='about'),
    url(r'download_resume/', views.download_resume, name='download_resume'),
]