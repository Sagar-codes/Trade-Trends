from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.stockTracker, name='stocktracker'),
    path('liveStocks', views.liveStocks, name='livestocks')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
