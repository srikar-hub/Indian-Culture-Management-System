from django.shortcuts import *

from .models import student, child


# Create your views here.
def home(request):
    return render(request,'home.html')

def books(request):
    return render(request,'Books.html')

def festive(request):
    return render(request,'FestiveSeason.html')

def temples(request):
    return render(request,'Temples.html')

def traditions(request):
    return render(request,'Traditions.html')

def adb(request):
    return render(request,'AthidiDevoBava.html')

def nails(request):
    return render(request,'nails.html')

def namaste(request):
    return render(request,'Namaste.html')

def am(request):
    return render(request,'ArrangedMarraige.html')

def holycow(request):
    return render(request,'HolyCow.html')

def about(request):
    return render(request,'About.html')

def contact(request):
    return render(request,'contact.html')
def signup(request):
    if request.method == "POST":
        firstname = request.POST.get('firstName')
        lastname = request.POST.get('lastName')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        password = request.POST.get('password')
        student.objects.create(firstName=firstname, lastName=lastname, email=email, dob=dob, password=password)
            # Redirect to the login page after successful signup
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            student.objects.get(email=email, password=password)
            return redirect('home')
        except student.DoesNotExist:
            return render(request,'login.html')
    return render(request, 'login.html')


def flipbook(request):
    return render(request,'flipbook.html')






from django.shortcuts import render, redirect
from .models import student, child

# Your other view functions here...

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Create Child object with lowercase field names
        child.objects.create(name=name, phonenumber=phonenumber, email=email, message=message)
        return render(request, 'success.html')
    return render(request, 'contact.html')



