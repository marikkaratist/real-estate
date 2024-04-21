from django.urls import path
from realty.views import (FlatListApi, FlatDetailApi, FloorListApi, FloorDetailApi, )

urlpatterns = [
    path('flats/', FlatListApi.as_view()),
    path('flats/<int:flat_id>/', FlatDetailApi.as_view()),
    path('floors/', FloorListApi.as_view()),
    path('floors/<int:flat_id>/', FloorDetailApi.as_view()),
]

