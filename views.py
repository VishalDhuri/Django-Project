from django.shortcuts import render , redirect
from .models import userr , fooditem , Review
from .forms import Createfood , CreateReview , Createuser , Newuser
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages

# Create your views here.

def index(request):
    data = Review.objects.all()
    return render(request,"index.html",{'data':data})

def usert(request):
    data = userr.objects.all()
    return render(request,"user.html",{'data':data})

def foddie(request):
    data = fooditem.objects.all()
    return render(request,"food.html",{'data':data})

def uploaduser(request):
    if request.method=='POST':
        form = Createuser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""Invalid data ,reload on<a href="{{ url : 'index'}}">reload</a> """)
    form = Createuser()
    return render(request,"upload.html",{"form":form})

def uploadfood(request):
    if request.method=='POST':
        form = Createfood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""Invalid data ,reload on<a href="{{ url : 'index'}}">reload</a> """)
    form = Createfood()
    return render(request,"upload.html",{"form":form})

def uploadreview(request):
    if request.method=='POST':
        form = CreateReview(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse("""Invalid data ,reload on<a href="{{ url : 'index'}}">reload</a> """)
    form = CreateReview()
    return render(request,"upload.html",{"form":form})

def editreview(request,uid):
    uid = int(uid)
    data = Review.objects.get(id=uid)
    form1 = CreateReview(request.POST or None,instance=data)
    if form1.is_valid():
        form1.save()
        return redirect('index')
    return render(request,"upload.html",{'form':form1})

def deleteR(request,rid):
    rid = int(rid)
    data = Review.objects.get(id=rid)
    data.delete()
    return redirect('index')

def edituser(request,uname):
    uname = str(uname)
    data = userr.objects.get(username =uname)
    forms = Createuser(request.POST or None,instance=data)
    if forms.is_valid():
        forms.save()
        return redirect('index')
    return render(request,"upload.html",{'form':forms})

def deleteU(request,uname):
    uname = str(uname)
    data = userr.objects.get(username=uname)
    data.delete()
    return redirect('user')

def editfood(request,fname):
    fname = str(fname)
    data = fooditem.objects.get(foodname=fname)
    form = Createfood(request.POST or None,instance=data)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,"upload.html",{'form':form})
        

def deleteF(request,fname):
    fname = str(fname)
    data = fooditem.objects.get(foodname=fname)
    data.delete()
    return redirect('index')

def CreateUser(request):
    if request.method=='POST':
        form = Newuser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,"Registration has Successfully")
            return redirect('login')
        messages.error(request,"invalid data")
    form = Newuser()
    return render(request,"register.html",{'register':form})

def sign_in(request):
    if request.method=='POST':
        form = AuthenticationForm(request,request.POST)    
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f"you are loggedin as {username}.")
                return redirect('index')
            messages.error(request,"invalid username and password")
        messages.error(request,"invalid username and password")
    form = AuthenticationForm()
    return render(request,"login.html",{'login':form})

def sign_out(request):
    logout(request)
    return redirect('index')
