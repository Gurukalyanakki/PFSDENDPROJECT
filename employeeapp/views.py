from django.shortcuts import render

# Create your views here.

def employeehomepagecall(request):
    return render(request,'employeeapp/employeehomepage.html')