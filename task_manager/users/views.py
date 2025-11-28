# from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView


class UsersIndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"