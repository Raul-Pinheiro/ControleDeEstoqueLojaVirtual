from django.urls import path 
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('cadastro',views.cadastro,name='cadastro'),
    path('login',views.login,name='login'),
    path('cadastro_db',views.cadastro_db,name='cadastro_db'),
    path('authLogin',views.authLogin,name='authLogin'), 
    path('localize',views.localize,name='localize'),  
    path('logout',views.logout,name='logout'),
    path('suporte',views.suporte,name='suporte'),
       
]