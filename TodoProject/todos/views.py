from django.shortcuts import render, redirect
from django.http import HttpRequest
from . models import Todo


# Create your views here.

def list_todo_items(request: HttpRequest):
    all_todos = Todo.objects.all()
    context = { "todo_list": all_todos }
    return render(request, "todos/todo_list.html", context=context)

def todo_item_detail(request: HttpRequest, todo_id: int):
    one_todo = Todo.objects.get(id=todo_id)
    context = { "todo_list": one_todo }
    return render(request, "todos/todo_list_detail.html", context=context)

def insert_todo_item(request: HttpRequest):
    todo = Todo()
    todo.content = request.POST["content"]
    todo.save()
    return redirect('/todos/list')

def delete_todo_item(request: HttpRequest, todo_id: int):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todos/list')

def update_todo_item(request: HttpRequest, todo_id: int):
    todo_to_update = Todo.objects.get(id=todo_id)
    todo_to_update.content = request.POST["textarea"]
    todo_to_update.save()
    return redirect('/todos/list')
