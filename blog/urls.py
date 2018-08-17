from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:post_id>/', views.detail, name='detail'),
    url(r'^$', views.index, name='index'),
]