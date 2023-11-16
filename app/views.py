from django.shortcuts import render

# Create your views here.
def username(request):
    d={'NAME':'BHANU'}
    return render(request,'username.html',context=d)
