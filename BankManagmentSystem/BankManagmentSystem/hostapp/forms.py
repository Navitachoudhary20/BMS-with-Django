from django import forms
from .models import Host
class HostForms(forms.ModelForm):
    class Meta:
        model = Host
        fields = "__all__"