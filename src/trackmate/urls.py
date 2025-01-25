from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("apps.tasks.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.profiles.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
