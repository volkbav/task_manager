from django.urls import path


from task_manager.users.views import (

    UserCreateView,
    UsersIndexView,
    UserUpdateView,
)

app_name = 'users'

urlpatterns = [
    path('', UsersIndexView.as_view(), name='users'),
    path("create/", UserCreateView.as_view(), name="create"),    
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
]