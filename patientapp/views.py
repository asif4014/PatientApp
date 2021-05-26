from django.shortcuts import render,redirect
from django.contrib import messages
from patientapp.models import UserInfo
# Create your views here.
def home(request):
    return render(request,'patientapp/index.html')

def addUserInfo(request):
    return render(request,'patientapp/regdform.html')

def fetchUserInfo(request):
    return render(request,'patientapp/fetch.html')

def register(request):
    if request.method=="POST":
        username = request.POST["username"]
        uniqueID = request.POST["uid"]
        dob = request.POST["dob"]

        obj = UserInfo(username=username,uniqueID=uniqueID,dob=dob)
        obj.save()
    messages.success(request,"Patient registerd successfully")
    return redirect(home)

def auth_user(request):
    if request.method == 'POST':
        uniqueID = request.POST['uid']

        if UserInfo.objects.filter(uniqueID=uniqueID):
            info = UserInfo.objects.filter(uniqueID=uniqueID)
            context = {'obj': info}
            return render(request,'patientapp/showinfo.html', context)
        else:
            messages.warning(request,f'OOPS!! Patient is not registered')
            return render(request,'patientapp/regdform.html')