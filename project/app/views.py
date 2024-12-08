from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

def todo(request):
    todos=todotable.objects.all()
    if request.method=='POST':
        todoarea=request.POST['todoarea']
        data=todotable.objects.create(sub=todoarea)
        data.save()
    return render(request,'index.html',{'todos':todos})

def todo_update(request,pk):
    data=todo.objects.get(pk=pk)
    print(data.sub)
    return render(request,'index2.html',{'data':data})
