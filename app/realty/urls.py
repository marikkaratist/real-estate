from django.urls import path
from realty.views import (FlatListApi, FlatDetailApi, FloorListApi, FloorDetailApi, FlatCreateApi)

urlpatterns = [
    path('flats/', FlatListApi.as_view()),
    path('flats/<int:pk>/', FlatDetailApi.as_view()),
    path('flats/create/', FlatCreateApi.as_view()),
    path('floors/', FloorListApi.as_view()),
    path('floors/<int:pk>/', FloorDetailApi.as_view()),
]

