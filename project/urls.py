from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.createProject, name='create-file'),
    path('update/<str:pk>/', views.updateProject, name='update-file'),
    path('delete/<str:pk>/', views.deleteProject, name='delete-file'),
]
