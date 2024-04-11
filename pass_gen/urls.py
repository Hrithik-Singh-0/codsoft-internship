from django.urls import path
from . import views

urlpatterns = [
    path('', views.pass_gen),
    path('password', views.password),
]