from django.urls import path

from task_manager.users.forms import UserFormLogin
from task_manager.users.views import (
    MyLoginView,
    MyLogoutView,
    UserFormCreateView,
    UsersIndexView,
)

app_name = 'users'

urlpatterns = [
    path('', UsersIndexView.as_view(), name='users'),
    path("create/", UserFormCreateView.as_view(), name="user_create"),
    path('login/', MyLoginView.as_view(
        template_name="registration/login.html",
        authentication_form=UserFormLogin,
    ), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
]