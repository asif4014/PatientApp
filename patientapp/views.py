from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from patientapp.models import EmpInfo
from django.core.files.storage import FileSystemStorage
import os

from django.conf import settings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
path = os.path.join(BASE_DIR, 'media/Resumes')

# Create your views here.


def home(request):
    return render(request, 'patientapp/index.html')


def addUserInfo(request):
    return render(request, 'patientapp/regdform.html')


def fetchUserInfo(request):
    return render(request, 'patientapp/fetch.html')


def register(request):
    if request.method == "POST":

        if request.FILES.get('resume'):

            print('Resume is coming.....')

            empname = request.POST.get("empname")
            mobile = request.POST.get("mobile")
            email = request.POST.get("email")
            skill = request.POST.get("skill")
            experience = request.POST.get("experience")

            resume = request.FILES['resume']

            fs = FileSystemStorage()

            print("File Name:", resume)

            file_name = resume.name
            path = "Resumes/" + file_name
            print("Ye path hai...", path)

            resume_path = os.path.join(settings.MEDIA_ROOT, file_name)
            print("Ye resume path hai........", resume_path)

            fs.save(file_name, resume)

            obj = EmpInfo(empname=empname, mobile=mobile,
                          email=email, experience=experience, skill=skill, resume=resume, resume_path=path)
            obj.save()
            messages.success(request, "Employee registerd successfully")
            return redirect(home)
    else:
        print("File didn't receive.")
        context = {'status': "Failed"}
        return JsonResponse(context)


def auth_user(request):
    if request.method == 'POST':
        skill = request.POST['skill']
        experience = request.POST['experience']

        if EmpInfo.objects.filter(skill=skill, experience=experience):
            info = EmpInfo.objects.filter(skill=skill, experience=experience)
            context = {'obj': info}
            return render(request, 'patientapp/showinfo.html', context)
        else:
            messages.warning(request, f'OOPS!! Employee is not found')
            return render(request, 'patientapp/regdform.html')
