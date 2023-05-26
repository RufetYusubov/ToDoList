from django.urls import path
from todo_list import views

urlpatterns = [
    path('todolist/',views.todolist,name="todolist")
]
