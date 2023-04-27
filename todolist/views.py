from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo


def index(request):
    todos = ToDo.objects.all()

    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})

@require_http_methods(['POST'])
def add(request):
    title = request.POST['title'] #title это название поля
    todo = ToDo(title=title)
    todo.save() # метод save сохраняет в базу данных
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id) # при помощи метода get ищем по id нашу todo_id
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')