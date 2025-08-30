from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    
    path('task/<int:task_id>/update/', views.UpdateCreateView.as_view(), name='add_update'),
]