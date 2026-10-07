from django.shortcuts import render

def home(request):
    return render(request, 'app1/base.html')

def about(request):
    return render(request, 'app1/about.html')

def contact(request):
    return render(request, 'app1/contact.html')