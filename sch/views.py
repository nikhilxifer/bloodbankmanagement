from django.shortcuts import render
from sch.models import search1
from sch.models import subs

# Create your views here.


def list(request):
    select1=request.POST.get('select1')
    select2=request.POST.get('select2')
    ls = search1.objects.filter(City=select2)
    print(select2)
    print(select1)
    return render(request,'search/search.html',{"ls1":ls})

def footer1(request):
    return render(request,'mid/index.html.carousel_32cb')

def subs1(request):
    if request.method=="POST":
        print("email submitted")
        email=request.POST['email']
        print(email)
    return render(request,'blood/index.html')
   

         
   
   