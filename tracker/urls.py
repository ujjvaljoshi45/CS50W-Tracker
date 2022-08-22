from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('trackrecord',views.trackRecord,name='trackRecord'),
    path('register',views.register,name='register'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('about',views.about,name='about'),

    #API
    path('api/addMoney',views.addMoney,name='addMoney'),
    path('api/addExpense',views.addExpense,name='addExpense'),
    path('api/getExpenses',views.getExpenses,name='getExpenses'),
    path('api/getTotalAmount',views.getTotalAmount,name='getTotalAmount'),
]