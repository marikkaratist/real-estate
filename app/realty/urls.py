from django.conf.urls.static import static
from django.urls import path

from app.config import settings
from views import (FlatListApi, FlatDetailApi)

urlpatterns = [
    path('flats/', FlatListApi.as_view()),
    path('flats/<int:flat_id>/', FlatDetailApi.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
