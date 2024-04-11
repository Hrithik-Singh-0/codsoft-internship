from django.urls import path
from . import views

urlpatterns = [
    path('', views.todolist),
    path('remove/<int:task_id>/', views.remove_task, name='remove_task'),

]