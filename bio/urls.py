from django.conf.urls import url
from . import views
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'bio'
urlpatterns = [

    path('', views.about),
    path('<str:prof>/about', views.about, name='about'),
    path('<str:prof>/download_resume', views.download_resume, name='download_resume'),
    path('<str:prof>/contact', views.contact, name='contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)