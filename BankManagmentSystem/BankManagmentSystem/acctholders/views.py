from django.shortcuts import render,redirect
from .models import AcctHolders
from .forms import AcctHoldersForm
# Create your views here.

def homepage(request):
    return render(request,'Bankhomepage.html')


def createaccount(request):
    if request.method == "POST":
        pswrd1 = request.POST['password1']
        pswrd2 = request.POST['password2']
        adhr = request.POST['aadhaar']
        acc_typ = request.POST['acc_typ']
        balance = int(request.POST['balance'])
        print(acc_typ)
        
        if acc_typ == "Current" and balance <= 50000:
            return render(request,'createaccount.html',{'msg':'Current Account Balance Should Be Greater Than 50000'})
        if acc_typ == "Saving" and balance <= 0:
            return render(request,'createaccount.html',{'msg':'Initial Balance Should Be Greater Than 0'})
        if pswrd1 == pswrd2:
            data = AcctHolders.objects.all().values_list()
            for a_no in data:
                if a_no[5] == adhr:
                    return render(request,'createaccount.html',{'msg':'Adhaar No is Already Registred'})
            else:
                form = AcctHoldersForm(request.POST)
                if form.is_valid():
                    try:
                        form.save()
                        return render(request,'login.html',{'msg':'Account Created Successfully'})
                    except Exception as e:
                        # print(e)
                        return render(request,'createaccount.html')
                else:
                    return render(request,'createaccount.html')
        
        else:
            return render(request,'createaccount.html',{'msg':'Passwords are not Matching'})
    else:
        return render(request,'createaccount.html')
   

def holder_homepage(request):
    username = request.POST['username']
    password = request.POST['password']
    data = AcctHolders.objects.all().values_list()
    for user in data:
        if username == user[2] and password == user[3]:     
            users = AcctHolders.objects.filter(email=username,password1=password).values()
            users_data = {
                'users':users
            }
            return render(request,'acctholder.html',users_data)
    else:
        return render(request,'login.html',{'msg':user})
    

def login(request):
    return render(request,'login.html')

# def forg_match(request,id)

def withdraw(request,id):
    user = AcctHolders.objects.get(id=id)
    data = {
        'user':user
    }
    return render(request,'widraw.html',data)

def wid_trans(request,id):
    if request.method== "POST":
        balance = int(request.POST['wid_amt'])
        data = AcctHolders.objects.filter(id=id).values_list()
        for bal in data:
            updated_balance = int(bal[9])
        if updated_balance > balance:
            updated_balance = updated_balance - balance
            AcctHolders.objects.filter(id=id).update(balance=updated_balance)
            user = AcctHolders.objects.filter(id=id).values()
            context = {
                'users':user
            }
            return render(request,'acctholder.html',context)
        else:
            user = AcctHolders.objects.filter(id=id).values()
            context = {
                'users':user,
                'msg':'Insufficient Balance',
            }
            return render(request,'acctholder.html',context)


def deposit(request,id):
    user = AcctHolders.objects.get(id=id)
    data = {
        'user':user
    }
    return render(request,'deposit.html',data)

def dep_trans(request,id):
    if request.method== "POST":
        data = AcctHolders.objects.filter(id=id).values_list()
        for bal in data:
            updated_balance = int(bal[9])
        balance = int(request.POST['dep_amt'])
        updated_balance = updated_balance + balance
        AcctHolders.objects.filter(id=id).update(balance=updated_balance)
        user = AcctHolders.objects.filter(id=id).values()
        context = {
            'users':user
        }
        return render(request,'acctholder.html',context)

def update(request,id):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        address = request.POST['address']
        phone = request.POST['phone']
        if password1 == password2:
            pass
        else:
            return render(request,'update.html',)

    else:
        user = AcctHolders.objects.filter(id=id).values()
        data = {
            "users":user,
        }
        return render(request,'update.html',data)
    
def save_update(request,id):
    name = request.POST['name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']
    address = request.POST['address']
    phone = request.POST['phone']
    if password1 == password2:
        AcctHolders.objects.filter(id=id).update(name=name,
                                                email=email,
                                                password1=password1,
                                                password2=password2,
                                                address=address,
                                                phone=phone)
        users = AcctHolders.objects.filter(id=id).values()
        return render(request,'usersdata.html',{'msg':'Data updates Successfullly','users':users})
    else:
        users = AcctHolders.objects.filter(id=id).values()
        return render(request,'update.html',{'users':users})
    

def delete(request,id):
    acc_hldr = AcctHolders.objects.filter(id=id)
    acc_hldr.delete()
    users = AcctHolders.objects.all().values()
    return render(request,'usersdata.html',{'users':users})