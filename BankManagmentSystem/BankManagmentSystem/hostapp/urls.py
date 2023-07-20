from django.urls import path
from . import views


urlpatterns = [
    path('',views.hostlogin,name='hostlogin'),
    path('log_check',views.usersdata,name='usersdata'),
    path('sortbyaccount',views.sortbyaccount,name='sortbyaccount'),
    path('sortbybalance',views.sortbybalance,name='sortbybalance'),
    path('sortbyname',views.sortbyname,name='sortbyname'),
    path('sortbycotact',views.sortbycotact,name='sortbycotact'),
    path('searchbyname',views.searchbyname,name='searchbyname'),
    path('showsearch',views.showsearch,name='showsearch'),
]