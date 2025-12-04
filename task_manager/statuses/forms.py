from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Status


class StatuseForm(ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
        labels = {
            'name': _("Name"),
        }
    