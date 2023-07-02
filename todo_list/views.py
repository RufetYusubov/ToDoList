from django.shortcuts import render, redirect
from todo_list.models import ToDoListModel
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(
                username=username,
                password=password
            )
        else:
            messages.info(request,"Username has been taken")

    return render(request,'signup.html')

#------------------------------------------------------
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You logged in")
            return redirect("buildingalist")
        else:
            if not User.objects.filter(username=username).exists():
                messages.info(request,"Please, enter correct username")
            else:
                messages.info(request, "Please, enter correct password")
    return render(request,'login.html')

#------------------------------------------------------
def logoutUser(request):
    logout(request)
    return redirect("login")
#------------------------------------------------------
def buildingalist(request):
    if not request.user.is_authenticated:
        raise Http404
    if request.method == "POST":
        name = request.POST.get('name')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        date = request.POST.get('date')


        ToDoListModel.objects.create(
            user = request.user,
            name = name,
            starttime = starttime,
            endtime = endtime,
            date = date,
        )
        return redirect("todolist")
    return render (request, 'buildingalist.html')
#------------------------------------------------------------------------
def todolist(request):
    if not request.user.is_authenticated:
        raise Http404
    todolists = ToDoListModel.objects.filter(
        user = request.user
    )
    context = {
        "todolists" : todolists
    }

    return render(request,'todolist.html',context)
#------------------------------------------------------------
def deletetodolist(request,id):
    todolist = ToDoListModel.objects.get(id=id)
    todolist.delete()
    return redirect("todolist")


