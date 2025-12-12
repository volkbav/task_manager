from django.urls import path

from .views import (
    LabelCreateView,
    LabelDeleteView,
    LabelsIndexView,
    LabelUpdateView,
)

app_name = 'labels'

urlpatterns = [
    path('', LabelsIndexView.as_view(), name='index'),
    path('create/', LabelCreateView.as_view(), name='create'),
    path('<int:pk>/delete/', LabelDeleteView.as_view(), name='delete'), 
    path('<int:pk>/update/', LabelUpdateView.as_view(), name='update'),
]