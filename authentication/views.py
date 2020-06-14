from django.shortcuts import render
from django.http import HttpResponse
from .models import User,UserProfile
# Create your views here.

def LoginView(request):
    if request.method == 'GET':
        return render(request, 'authentication/form.html', context={"messages": "Details Received"})
    elif request.method == 'POST':
        email = request.POST.get("emailId")
        password = request.POST.get("exampleInputPassword1")
        u =User.objects.create(email=email,password=password)
        u.save()
        return render(request, 'authentication/form.html', context={"messages": "TRIGGERED"})

def BasePageView(request):
    return render(request,"base.html",context = {"message":"Home page triggered"})

def LoginView(request):
    if request.method == 'GET':
        return render(request,'',context={"message":"Detail Received"})
    elif request.method == 'POST':
        emailid = request.POST.get("emailId")
        count = UserProfile.objects.all().count()
        email = UserProfile.objects.values("email")
        for i in range(count):
            if emailid in email[i]["email"]:
                return HttpResponse("<h1>This email id already exist in the system. Try with another email</h1>")
        password = request.POST.get("exampleInputPassword1")
        firstname = request.POST.get("first-name")
        lastname = request.POST.get("last-name")

        return render(request,'',context={"message":"Triggered"})