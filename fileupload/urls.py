from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('fileupload', views.index, name='index'),
    path('filtering', views.filtering, name='filtering'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

