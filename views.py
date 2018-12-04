from django.http import HttpResponse
from django import render

def index(request):
    return HttpResponse('Helllo World')

def login(request):
    return render(request, 'app/login.html')
