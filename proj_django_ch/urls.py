from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from proj_django_ch import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('handball_app.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)