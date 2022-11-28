from django.shortcuts import render
from .models import Doctors,Departments

from .forms import BookingForm

def index(request):
    return render(request,'home.html') 
    
def about(request):
    return render(request,'about.html') 


def booking(request):
    if request.method=="POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form) 


def departments(request):
    dict_dpt={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dpt)


def contactus(request):
    return render(request,'contactus.html')   


def doctors(request):
    dict_docs={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)                             

# Create your views here.
