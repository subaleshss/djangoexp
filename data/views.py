from django.shortcuts import render,redirect
from .models import datacol
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'home.html')

def getdata(request):
    if request.method=='POST':
        nm=request.POST['name']
        ag=request.POST['age']

        dts=datacol.objects.create(name=nm,age=ag)
        dts.save();
        return redirect('/')

def viewdata(request):
    dt=datacol.objects.all()
    c = request.user
    n=c.username
    return render(request,'view.html',{'d':dt,'na':n})
