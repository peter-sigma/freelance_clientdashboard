from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)

    @property
    def overall_progress(self):
        """Calculate project progress based on tasks (Pythonic showcase)."""
        tasks = self.tasks.all()
        if not tasks:
            return 0
        total_progress = sum(task.progress for task in tasks) / len(tasks)
        return round(total_progress, 2)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField(null=True, blank=True)

    @property
    def progress(self):
        # Simple logic for progress (customize as needed)
        return {'pending': 0, 'in_progress': 50, 'completed': 100}.get(self.status, 0)

    def __str__(self):
        return self.title

class ProgressUpdate(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='updates')
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Update for {self.task.title}"