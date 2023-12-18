from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from app112.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app112.urls', namespace='app112'))  # подключение всех app112.urls к url 'app112/'
]

handler404 = page_not_found

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
