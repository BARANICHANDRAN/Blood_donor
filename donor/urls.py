from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('donor_list/', views.donor_list, name='donor_list'),
    path('view/', views.view_donor, name='view_donor'),
    path('add/', views.add_donor, name='add_donor'),
    path('edit/<str:contact>/', views.edit_donor, name='edit_donor'),
]
