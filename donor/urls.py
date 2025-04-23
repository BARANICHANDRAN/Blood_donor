from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_donor, name='add_donor'),
    path('edit/<str:contact>/', views.edit_donor, name='edit_donor'),
    path('', views.donor_list, name='donor_list'),
]
