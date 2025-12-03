
# Create your views here.
# from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _
from .forms import UserFormCreate, UserFormLogin




# path ''
class UsersIndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


# path 'create/
class UserFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserFormCreate()
        return render(request, "users/create.html", {"form": form})
        
    def post(self, request, *args, **kwargs):
        form = UserFormCreate(request.POST)
        if form.is_valid():  # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.info(request, _("User created"))
            return redirect('users:login')  # Редирект на указанный маршрут
        # Если данные некорректные, то возвращаем человека обратно 
        # на страницу с заполненной формой
        messages.error(request, _("Login failed"))
        return render(request, 'users/create.html', {'form': form})

class MyLoginView(LoginView):
    form_class = UserFormLogin
    template_name = "registration/login.html"

    def form_valid(self, form):
        messages.success(self.request, _("Logged in successfully"))
        return super().form_valid(form)
    
class MyLogoutView(LogoutView):
    next_page = 'users:login'

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _("You have logged out"))
        return super().dispatch(request, *args, **kwargs)