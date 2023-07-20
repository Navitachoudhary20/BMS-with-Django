from django import forms
from acctholders.models import AcctHolders

class AcctHoldersForm(forms.ModelForm):
    class Meta:
        model = AcctHolders
        fields = "__all__"
