from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'), #accounts로 들어올떄 유저 목록 제공
    path('create/', views.create, name='create'), #accounts로 들어올떄 유저 목록 제공
    path('login/', views.login, name='login'), #accounts로 들어올떄 유저 목록 제공
    path('logout/', views.logout, name='logout'), #accounts로 들어올떄 유저 목록 제공
    path('delete/', views.delete, name='delete'), #accounts로 들어올떄 유저 목록 제공
    path('update/', views.update, name='update'), #accounts로 들어올떄 유저 목록 제공
    path('password/', views.change_password, name='change_password'), #accounts로 들어올떄 유저 목록 제공
]
