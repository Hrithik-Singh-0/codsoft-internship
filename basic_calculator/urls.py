from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_calc),
    path('result', views.calc_result),
]