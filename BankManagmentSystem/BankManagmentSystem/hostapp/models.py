from django.db import models

# Create your models here.
class Host(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'host_table'