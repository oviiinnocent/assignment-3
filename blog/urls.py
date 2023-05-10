from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.Home, name = 'home'),
    path('blog/', views.Blog, name= 'blog'),
    path('<slug:slug>', views.single_post, name = 'single_post'),
    path('category/<slug:slug>/', views.category, name='category'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)