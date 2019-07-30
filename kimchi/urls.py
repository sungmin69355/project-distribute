from django.contrib import admin
from django.urls import path, include
import kmain.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', kmain.views.home, name= "home"),
    path('kimchi/', include('kmain.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


