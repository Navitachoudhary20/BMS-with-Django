from django.shortcuts import render
from acctholders.models import AcctHolders
from .models import Host
from django.contrib import messages
# Create your views here.
def hostlogin(request):
    return render(request,'hostlogin.html')


def usersdata(request):
    username = request.POST['username']
    password = request.POST['password']
    data = Host.objects.all().values_list()
    for info in data:
        if username == info[1] and password == info[2]:
            users = AcctHolders.objects.all().values()
            users_data = {
                'users':users
            }
            return render(request,'usersdata.html',users_data)
    else:
        return render(request,'hostlogin.html',{'msg':'Invalid Credentials'})
def sortbyaccount(request):
    users = AcctHolders.objects.all().order_by('id').values()
    users_data = {
        'users':users,
    }
    return render(request,'usersdata.html',users_data)

def sortbybalance(request):
    users = AcctHolders.objects.all().order_by('balance').values()
    users_data = {
        'users':users,
    }
    return render(request,'usersdata.html',users_data)

def sortbyname(request):
    users = AcctHolders.objects.all().order_by('name').values()
    users_data = {
        'users':users
    }
    return render(request,'usersdata.html',users_data)

def sortbycotact(request):
    users = AcctHolders.objects.all().order_by('phone').values()
    users_data = {
        'users':users
    }
    return render(request,'usersdata.html',users_data)


def searchbyname(request):
    return render(request,'search.html')

def showsearch(request):
    name = request.POST['name']
    users = AcctHolders.objects.filter(name=name).values()
    if users:
        users_data = {
        'users':users,
        }
        return render(request,'usersdata.html',users_data)
    else:
        return render(request,'search.html',{'msg':'User Not Found'})