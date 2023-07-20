from django.urls import path,include
from acctholders import views

# log_check
urlpatterns = [
    path('hst',views.hostlogin,name='hostlogin'),
    path('log_check',views.usersdata,name='usersdata'),
    path('sortbyaccount',views.sortbyaccount,name='sortbyaccount'),
    path('sortbybalance',views.sortbybalance,name='sortbybalance'),
    path('sortbyname',views.sortbyname,name='sortbyname'),
    path('sortbycotact',views.sortbycotact,name='sortbycotact'),
    path('searchbyname',views.searchbyname,name='searchbyname'),
    path('showsearch',views.showsearch,name='showsearch'),
    path('transactions',views.transactions,name='transactions'),



    path('',views.homepage,name='homepage'),
    path('reg_match',views.createaccount,name='createaccount'),

    path('back/<int:id>',views.holder_homepage,name='holder_homepage'),

    path('log_user',views.holder_homepage,name='holder_homepage'),
    path('login',views.login,name='login'),
    
    path('withdraw/<int:id>',views.withdraw,name='withdraw'),
    path('wid_trans/<int:id>',views.wid_trans,name='wid_trans'),

    path('deposit/<int:id>',views.deposit,name='deposit'),
    path('dep_trans/<int:id>',views.dep_trans,name='dep_trans'),

    path('update/<int:id>',views.update,name='update'),
    path('save_update/<int:id>',views.save_update,name='save_update'),

    path('delete/<int:id>',views.delete,name='delete'),

    path('reset_pass',views.reset_pass,name='reset_pass'),
    path('forgot_pass',views.forgot_pass,name='forgot_pass'),

    path('transact_user/<int:id>',views.transact_user,name='transact_user'),
    
    path('back/<int:id>',views.holder_homepage,name='holder_homepage'),


]#/transactions/{{user.id}}