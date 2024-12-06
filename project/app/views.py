from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    # return redirect(index2)
 return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')
