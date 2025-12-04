from django.urls import path

from task_manager.statuses.views import StatusCreateView, StatusIndexView

app_name = 'statuses'

urlpatterns = [
    path('', StatusIndexView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='create'),
]