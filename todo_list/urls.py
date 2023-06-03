from django.urls import path
from todo_list import views

urlpatterns = [
    path('buildingalist/',views.buildingalist,name="buildingalist"),
    path('todolist/',views.todolist,name="todolist"),
    path('signup/',views.signup, name = "signup"),
    path('login/',views.loginUser,name="login"),
    path('logout/',views.logoutUser,name = "logout"),
    path('delete/<int:id>/',views.deletetodolist, name= "delete")
]
