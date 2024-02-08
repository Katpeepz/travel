from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
from .models import new
from .models import tuba
from .models import tuba1

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1=new.objects.all()
    obj2=tuba.objects.all()
    obj3=tuba1.objects.all()
    return render(request,"index.html",{'result':obj,'res':obj1,'res1':obj2,'res2':obj3})
