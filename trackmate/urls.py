from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from tasks import views

urlpatterns = i18n_patterns(
    # General urls
    path("admin/", admin.site.urls),
    path("", include("tasks.urls")),
    path("", include("users.urls")),
    path("", include("profiles.urls")),
    # Set language
    path("set_language/", views.SetLanguageView.as_view(), name="set-language"),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
