from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

# Create
def create(request):
    if request.method == 'POST':
        myform = TaskForm(request.POST)
        if myform.is_valid():
            myform.save()
            return redirect('home')
    else:
        myform = TaskForm()
    return render(request, 'create.html', {'myform': myform})


# Read
def home(request):
    tasks = Task.objects.all()
    return render(request, 'home.html', {'tasks':tasks})


# Update
def update(request):
    pass


# Delete
def delete(request):
    pass