from django.urls import path, include

from .views import (
    ClientListAPIView,
    ClientDetailAPIView,
    ClientUpdateAPIView,
    ClientDeleteAPIView,
    ClientCreateAPIView
)

app_name = 'todo-api'
urlpatterns = [

    path('', ClientListAPIView.as_view(), name='list'),
    path('create/', ClientCreateAPIView.as_view(), name='create'),
    path('<pk>/', ClientDetailAPIView.as_view(), name='detail'),
    path('<pk>/edit/', ClientUpdateAPIView.as_view(), name='update'),
    path('<pk>/delete/', ClientDeleteAPIView.as_view(), name='delete'),

]