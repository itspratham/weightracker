from django.urls import path
from .views import RegisterView,BasePageView,LoginView

urlpatterns =[
    path('',BasePageView,name = "base-page"),
    path('register/',RegisterView,name = "registerview"),
    path('login/',LoginView,name = "loginview")

]