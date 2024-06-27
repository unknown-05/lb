from django.shortcuts import render

def home(request):
    return render(request,'home.html')
def About_us(request):
    return render(request,'about_us.html')
def Contact_us(request):
    return render(request,'contact_us.html')