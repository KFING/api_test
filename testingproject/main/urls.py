from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('confirm_email/', views.registration, name = 'reg'),
    path('registration/', views.confirm_user, name = 'confirm_user'),
    path('reset_password/', views.reset, name = 'reset_password'),
    path('main/', views.main, name = 'main')
]
