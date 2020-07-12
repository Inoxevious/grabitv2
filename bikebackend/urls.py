from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('api/', include('api.urls')),
    path('o/', include('oauth2_provider.urls')),
    path('doc/', include('rest_framework_docs.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('admin/', admin.site.urls),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)