from django.shortcuts import render
from todo_list.models import ToDoListModel
from django.contrib import messages

def todolist(request):
    if request.method == "POST":
        name = request.POST.get("name")
        starttime = request.POST.get("starttime")
        endtime = request.POST.get("endtime")
        date = request.POST.get("date")
        status = request.POST.get("status")


        ToDoListModel.objects.create(
            name = name,
            starttime = starttime,
            endtime = endtime,
            date = date,
            status = status
        )
        messages.success(request, "qeyde alindi")
    return render (request, 'todolist.html')
