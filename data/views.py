from django.shortcuts import render,redirect
from .models import datacol

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
    return render(request,'view.html',{'d':dt})
