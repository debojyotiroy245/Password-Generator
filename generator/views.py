from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html',{'password':'gdgcddjhcjh'})

def password(request):
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    
    length = int(request.GET.get('length'))
    
    if(request.GET.get('uppercase')):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    
    if(request.GET.get('number')):
        characters.extend(list('0123456789'))
    
    if(request.GET.get('special')):
        characters.extend(list('!@#$%^&*()'))

    thePassword=''

    for _ in range(length):
        thePassword += random.choice(characters)
    return render(request,'generator/password.html',{'password':thePassword})

def about(request):
    # return HttpResponse('About')
    return render(request,'generator/about.html')