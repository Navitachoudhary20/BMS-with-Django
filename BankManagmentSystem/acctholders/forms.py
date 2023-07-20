from django import forms
from acctholders.models import AcctHolders,Transactions



class AcctHoldersForm(forms.ModelForm):
    class Meta:
        model = AcctHolders
        fields = "__all__"
class TransactionsForms(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = "__all__"



from django import forms
from .models import Host
class HostForms(forms.ModelForm):
    class Meta:
        model = Host
        fields = "__all__"