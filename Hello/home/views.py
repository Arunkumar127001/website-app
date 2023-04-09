from django.shortcuts import render,HttpResponse
from .models import Data
# Create your views here.
def home(request):
    if request.method=="POST":
        last_name=request.POST.get('last_name')
        first_name=request.POST.get('first_name')
        city=request.POST.get('city')
        state=request.POST.get('state')
        email=request.POST.get('email')
        zip=request.POST.get('zip')
        fill=Data(last_name=last_name,first_name=first_name,city=city,email=email,zip=zip,state=state)
        fill.save()
    return render(request,'home.html')



def about(request):
    return render(request,'about.html')
    
    # return HttpResponse('This is about page')

def admission(request):
    return render(request,'admission.html')


def signup(request):
    return render(request,'signup.html')

def students(request):
    return render(request,'students.html')


def contact(request):
    return render(request,'contact.html')