from django.shortcuts import render

# Create your views here.
def mahi(request):
    return render(request,'mahi.html')

def abc(request):
    return render(request,'mahi1.html')
def kiran(request):
    return render(request,'mahi2.html')
def raji(request):
    return render(request,'mahi3.html')

