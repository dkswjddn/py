from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name = 'list'),
    path('list/<int:id>/', views.detail, name='detail'),
]
