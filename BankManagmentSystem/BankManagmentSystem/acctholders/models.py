from django.db import models

# Create your models here.
class AcctHolders(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    aadhaar = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    acc_typ = models.CharField(max_length=50,null="True")
    balance = models.IntegerField(null="True")
    class Meta:
        db_table = "acct_holders"