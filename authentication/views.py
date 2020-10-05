from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import User,UserProfile
# Create your views here.
import logging
logger = logging.getLogger(__name__)

def RegisterView(request):
    if request.method == 'GET':
        return render(request, 'authentication/register.html', context={"messages": "Details Received"})
    elif request.method == 'POST':
        email = request.POST.get("emailId")
        print(email)
        password = request.POST.get("exampleInputPassword1")
        print(password)
        u =User.objects.create(email=email,password=password)
        u.save()
        logger.info("Created user "+str(request.POST))
        return render(request, 'authentication/register.html', context={"messages": "TRIGGERED"})

def BasePageView(request):
    return render(request,"base.html",context = {"message":"Home page triggered"})

def LoginView(request):
    if request.method == 'GET':
        return render(request,'authentication/login.html',context={"message":"Detail Received"})
    elif request.method == 'POST':
        print(request.POST)
        emailid = request.POST.get("emailId")
        count = User.objects.all().count()
        email = User.objects.values("email")
        for i in range(count):
            if emailid in email[i]["email"]:
                password = request.POST.get("exampleInputPassword1")
                firstname = request.POST.get("First name")
                lastname = request.POST.get("Last name")
                dob = request.POST.get("DOB")
                weight = request.POST.get("weight")
                image = request.POST.get("image")
                data = UserProfile()
                data.email = emailid
                data.password = password
                data.first_Name = firstname
                data.last_Name = lastname
                data.Dob = dob
                data.weight = weight
                data.photo = image
                data.save()
                return render(request, 'authentication/login.html', context={"message": "Triggered"})
    return reverse("registerview")