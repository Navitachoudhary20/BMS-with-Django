from django.urls import path,include
from acctholders import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('reg_match',views.createaccount,name='createaccount'),

    path('log_check',views.holder_homepage,name='holder_homepage'),
    path('login',views.login,name='login'),
    # path('forg_match',views.forg_match,name='forg_match'),
    

    path('withdraw/<int:id>',views.withdraw,name='withdraw'),
    path('wid_trans/<int:id>',views.wid_trans,name='wid_trans'),

    path('deposit/<int:id>',views.deposit,name='deposit'),
    path('dep_trans/<int:id>',views.dep_trans,name='dep_trans'),

    path('update/<int:id>',views.update,name='update'),
    path('save_update/<int:id>',views.save_update,name='save_update'),
    path('delete/<int:id>',views.delete,name='delete'),


]