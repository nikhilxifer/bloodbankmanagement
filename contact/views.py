from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        print(name,email,message)
        c = Contact(name=name, email=email, message=message )
        c.save()
        
    return render(request,'contact/contact.html')