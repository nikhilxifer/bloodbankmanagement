from django.shortcuts import render, return, HttpResponse
from footer.models import Subs
from django.contrib import messages

# Create your views here.


def subs(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subs =  Subs(email=email)
        subs.save()
        messages.success(request, 'You are subscribed')
        
    return render(request,'index.html')

