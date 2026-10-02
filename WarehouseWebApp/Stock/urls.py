from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

app_name = 'Stock'
urlpatterns = [
    # path('register', views.register, name='reg'),
    path('', views.home, name='home'),
    path('ViewItem/', views.view_item, name='View_Item'),
    path('AddItem/', views.add_item, name='add_item'),
    # path('login/', auth_views.LoginView.as_view(template_name='Stock/login.html'), name='login'),
    # path('login/', auth_views.LoginView.as_view(template_name='Stock/login.html'), name='login'),

    # path('logout/', views.Logout, name='logout'),
    path('index/', views.home, name='index')
]

