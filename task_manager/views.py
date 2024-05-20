from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from task_manager.models import TaskType, Position, Worker


@login_required
def index(request):
    """View function for the home page of the site"""
    num_workers = Worker.objects.count()
    num_positions = Position.objects.count()
    num_task_types = TaskType.objects.count()

    context = {
        "num_workers": num_workers,
        "num_positions": num_positions,
        "num_task_types": num_task_types,
    }

    return render(request, "task_manager/index.html", context=context)
