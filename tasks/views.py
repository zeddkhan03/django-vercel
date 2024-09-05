from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task
from .forms import TaskForm

def task_list(request):
    # Handle sorting/filtering based on query parameters
    status_filter = request.GET.get('status')
    sort_by = request.GET.get('sort_by')

    # Retrieve tasks
    tasks = Task.objects.all()

    # Apply status filter if provided
    if status_filter:
        tasks = tasks.filter(status=status_filter)
    
    # Apply sorting if specified
    if sort_by == 'priority':
        tasks = tasks.order_by('priority')
    elif sort_by == 'due_date':
        tasks = tasks.order_by('due_date')

    # Separate completed tasks
    completed_tasks = Task.objects.filter(status='Done', due_date__lt=timezone.now())
    incomplete_tasks = tasks.exclude(id__in=completed_tasks.values_list('id', flat=True))

    # Handle form submission
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # Reload the page to see new task
    else:
        form = TaskForm()
    
    context = {
        'tasks': incomplete_tasks,
        'completed_tasks': completed_tasks,
        'form': form
    }
    return render(request, 'tasks/task_list.html', context)

def delete_task(request, task_id):
    # Retrieve the task to be deleted
    task = get_object_or_404(Task, id=task_id)
    
    # Delete the task
    task.delete()
    
    # Redirect to the task list page
    return redirect('task_list')

def edit_task(request, task_id):
    # Retrieve the task to be edited
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    
    context = {
        'form': form,
        'task': task
    }
    return render(request, 'tasks/edit_task.html', context)
