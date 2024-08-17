from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/969d95f0-42ed-4e6b-ae78-55e2a13c1ae1", admin.site.urls),
    path('csp/', include('contentsecurity.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
