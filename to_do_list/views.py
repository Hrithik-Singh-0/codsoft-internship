from django.shortcuts import render, redirect
from .models import Tasks


def todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        tasks = Tasks(title=title)
        tasks.save()
    tasks = Tasks.objects.all()

    return render(request, 'to_do_list/todolist.html', {'tasks': tasks})



def remove_task(request, task_id):
    Tasks.objects.filter(id=task_id).delete()
    return redirect('/todolist')
