from django.urls import path
from realty.views import (FlatListApi, FlatDetailApi)

urlpatterns = [
    path('flats/', FlatListApi.as_view()),
    path('flats/<int:flat_id>/', FlatDetailApi.as_view()),
]

