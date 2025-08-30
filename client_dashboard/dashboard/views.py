from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Project, Task, ProgressUpdate
from .forms import ProgressUpdateForm

class DashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(client=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Data for Chart.js (portfolio shine)
        projects = self.get_queryset()
        status_counts = {'pending': 0, 'in_progress': 0, 'completed': 0}
        for project in projects:
            for task in project.tasks.all():
                status_counts[task.status] += 1
        context['status_counts'] = status_counts
        return context

class UpdateCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ProgressUpdate
    form_class = ProgressUpdateForm
    template_name = 'dashboard/update_form.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        # Only superusers (you) can add updates
        return self.request.user.is_superuser

    def form_valid(self, form):
        # Ensure task belongs to a project you manage
        form.instance.task = Task.objects.get(id=self.kwargs['task_id'])
        return super().form_valid(form)

def custom_logout(request):
    logout(request)
    return redirect('login')