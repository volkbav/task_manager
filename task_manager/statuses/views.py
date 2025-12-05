from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import ListView

from .forms import StatuseForm
from .mixins import StatusRequreMessageMixin
from .models import Status

# Create your views here.


# path ''
class StatusIndexView(StatusRequreMessageMixin, ListView):
    model = Status
    template_name = "statuses/index.html"
    context_object_name = "statuses"


# path 'create/'
class StatusCreateView(StatusRequreMessageMixin, View):
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


# path 'delete'
class StatusDeleteView(StatusRequreMessageMixin, View):
    def get(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        name = Status.objects.get(pk=status_pk).name
        context = {
            "status_pk": status_pk,
            "name": name,
        }
        return render(
            request,
            "statuses/delete.html",
            context
        )
    
    def post(self, request, *args, **kwargs):
        status_pk = kwargs.get('pk')
        status = Status.objects.get(pk=status_pk)
        if status:
            status.delete()
            messages.success(request, _("Status successfully deleted"))
            return redirect('statuses:statuses')  # Редирект на указанный маршрут
        messages.error(request, _('Ooops'))
        return redirect('statuses:statuses')
