from django.contrib import admin
from django.urls import path, include
from .views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('category/<slug:category_slug>/', index, name='post_by_category'),
    path('user/', include('User.urls')),
    path('post/', include('Posts.urls')),
    path('categoty/', include('Category.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)