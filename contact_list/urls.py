from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts),
    path('delete/<str:name>/', views.delete_contact, name='del_contact'),
    path('update/<str:name>/', views.update_contact, name='update_contact'),
]