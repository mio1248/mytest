from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('gallery/', include('board.urls')),
    path('accounts/login/', views.ShopLoginView.as_view(), name='login'),
    path('accounts/logout/', views.ShopLogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'shop' / 'static')
