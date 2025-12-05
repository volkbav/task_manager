from django.urls import path

from .views import TasksIndexView

app_name = 'tasks'

urlpatterns = [
    path('', TasksIndexView.as_view(), name='tasks'),
]