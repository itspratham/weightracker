from django.urls import path
from .views import LoginView,BasePageView

urlpatterns =[
    path('',BasePageView,name = "base-page"),
    path('login/',LoginView,name = "registerview")

]