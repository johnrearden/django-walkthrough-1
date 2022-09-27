from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
