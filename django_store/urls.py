from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cart/', include('cart.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('order/', include('orders.urls')),
    path('accounts/', include('allauth.urls')),
    path('contact/', include("contact.urls")),
    path('', include('store.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
