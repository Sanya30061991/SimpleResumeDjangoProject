from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main', views.start, name="home"),
    path('sites-info', views.webPages, name="sites"),
    path('skills', views.skill, name="skills"),
    path('contacts', views.contacts, name="contacts")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)