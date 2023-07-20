from django.shortcuts import render,redirect
from .models import AcctHolders,Transactions
from .forms import AcctHoldersForm
from .models import Host
import datetime,re
# Create your views here.

def homepage(request):
    return render(request,'Bankhomepage.html')

def createaccount(request):
    if request.method == "POST":
        name = request.POST['name'] 
        for i in name:
            if re.match('^[0-9]+$',i):
                return render(request,'createaccount.html',{'msg':'Invalid name'})
        pswrd1 = request.POST['password1']
        pswrd2 = request.POST['password2']
        adhr = request.POST['aadhaar']
        acc_typ = request.POST['acc_typ']
        balance = int(request.POST['balance'])
        phone = int(request.POST['phone'])
        email = request.POST['email']
        data = AcctHolders.objects.all().values_list()

        def validate_password(password):
            pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"
            if re.match(pattern, password):
                return True
            else:
                return False
        validation = validate_password(pswrd1) 
        if validation == True:      
            for no in data:
                if phone == int(no[7]):
                    return render(request,'createaccount.html',{'msg':'Mobile Number is Already Registered'})
                
            for no in data:
                if email == no[2]:
                    return render(request,'createaccount.html',{'msg':'Email Id is Already Registered'})
                
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
                            return render(request,'createaccount.html')
                    else:
                        return render(request,'createaccount.html')
            
            else:
                return render(request,'createaccount.html',{'msg':'Passwords are not Matching'})
        else:
            return render(request,'createaccount.html',{"msg":"Invalid Password"})
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
        return render(request,'login.html',{'msg':'Invalid Credentials'})
    

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
        if updated_balance >= balance:
            updated_balance = updated_balance - balance
            AcctHolders.objects.filter(id=id).update(balance=updated_balance)
            user = AcctHolders.objects.filter(id=id).values()
            context = {
                'users':user
            }
            x=str(datetime.datetime.now())
            trans_amt = Transactions(account_no=id,trans_typ="Widraw",amount=balance,date=x)
            trans_amt.save()
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
        x=str(datetime.datetime.now())
        dep_amt = Transactions(account_no=id,trans_typ="Deposit",amount=balance,date=x)
        dep_amt.save()
        context = {
            'users':user
        }
        return render(request,'acctholder.html',context)

def transact_user(request,id):
    transactions = Transactions.objects.filter(account_no=id).values()
    data ={
        'transactions':transactions
    }
    return render(request,'transactions.html',data)

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
        users = AcctHolders.objects.all().values()
        return render(request,'usersdata.html',{'msg':'Data updates Successfullly','users':users})
    else:
        users = AcctHolders.objects.filter(id=id).values()
        return render(request,'update.html',{'users':users})
    

def delete(request,id):
    acc_hldr = AcctHolders.objects.filter(id=id)
    acc_hldr.delete()
    users = AcctHolders.objects.all().values()
    return render(request,'usersdata.html',{'users':users})


def reset_pass(request):
    return render(request,'forgotpass.html')


def  forgot_pass(request):
    if request.method =="POST":
        acct = int(request.POST['acct'])
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        data = AcctHolders.objects.filter(id=acct).values_list()
        for info in data:
            if acct == int(info[0]):
                if password1 == password2:
                    AcctHolders.objects.filter(id=acct).update(password1=password1,password2=password2)
                    return render(request,'login.html',{'msg':'Password Reset successfully'})
                else:
                    return render(request,'forgotpass.html',{'msg':'Passwords Not Matching'})
            else:
                return render(request,'forgotpass.html',{'msg':'Entered Account Number Is Is Invalid'})

        else:
            return render(request,'forgotpass.html',{'msg':'Entered Account Number Is Is Invalid'})
        

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
    
def transactions(request):
    transactions = Transactions.objects.all().values()
    print(transactions)
    data = {
        'transactions':transactions
    }
    return render(request,'alltransactions.html',data)