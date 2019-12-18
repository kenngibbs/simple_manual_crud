from django.urls import path
from . import views

urlpatterns = [
    path('edit/<int:testID>/', views.edit, name="edit"),
    path('delete/<int:testID>/', views.delete, name="delete"),
    path('', views.index, name="index"),
]