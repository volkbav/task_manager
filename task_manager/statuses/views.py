from django.views.generic import ListView
from django.views import View
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatuseForm
from django.contrib import messages

# Create your views here.


# path ''
class StatusIndexView(ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"

# path 'create/'
class StatusCreateView(View):
    def get(self, request, *args, **kwargs):
        form = StatuseForm()
        return render(request, "statuses/create.html", {"form": form})
        
    def post(self, request, *args, **kwargs):
        form = StatuseForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, _("The status was created successfully"))
            return redirect('statuses:statuses') 
        
        return render(request, 'statuses/create.html', {'form': form})
