from django.urls import path
from . import views

urlpatterns = [
    path('api/todo/', views.TodoCreate.as_view()),
]
