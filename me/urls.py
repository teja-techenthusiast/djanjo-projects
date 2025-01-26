from django.contrib import admin
from django.urls import path, include # to know about our project path we import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', include('travello.urls')),
    path('admin/', admin.site.urls),
    #path('accounts/',include('accounts.urls')),
    #path('', include('base.urls')),
    path('', include('dashboard.urls')),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

