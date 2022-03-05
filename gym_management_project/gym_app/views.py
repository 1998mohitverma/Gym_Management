from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Enquiry, Plan, Equipment, Member
# Create your views here.

def home_page(request):
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.all()
    plan = Plan.objects.all()    
    equipment = Equipment.objects.all()    
    member = Member.objects.all()

    enq,pl,equ,mem = 0,0,0,0                
    
    for i in enquiry:
        enq+=1
    for i in plan:
        pl+=1
    for i in equipment:
        equ+=1
    for i in member:
        mem+=1

    context = {'enq':enq,'pl':pl,'equ':equ,'mem':mem}
                    
    return render(request, 'gym/home.html',context)    

def login_page(request):
    if not request.user.is_staff:
        error=''
        if request.method == 'POST':
            uname = request.POST['user']
            pwd = request.POST['pwd']
            user = authenticate(username=uname, password=pwd)
            try:
                if user.is_staff:
                    login(request,user)
                    error='no'
                else:
                    error='yes'    
            except:
                error='yes'
        context = {'error':error}        
        return render(request,'gym/login.html',context)
    else:
        return redirect('home')

def user_logout(request):
    if request.user.is_staff:
        logout(request)
        return redirect('login')
    else:
        return redirect('login')

#--start Enquiry code:-----------------------------------------------
def add_enquiry(request):
    if not request.user.is_staff:
        return redirect('login')
    error=''    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']    
        contact = request.POST['contact']    
        age = request.POST['age']    
        gender = request.POST['gender']    
        date = request.POST['date']
        try:
            Enquiry.objects.create(name=name,email=email,contact=contact,age=age,gender=gender,date=date)
            error='no'
        except:
            error='yes'
    context = {'error':error}        
    return render(request, 'gym/add_enquiry.html',context)    

def view_enquiry(request):
    if not request.user.is_staff:
        return redirect('login')
    enquiry = Enquiry.objects.all()
    context = {'enq':enquiry}    
    return render(request, 'gym/view_enquiry.html',context)

def delete_enquiry(request,id):
    if not request.user.is_staff:
        return redirect('login')
    enq = Enquiry.objects.get(pk=id)
    enq.delete()
    return redirect('view_enquiry')    

#--start Equipment code:-----------------------------------------------
def add_equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ''    
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']    
        unit = request.POST['unit']    
        date = request.POST['date']    
        cname = request.POST['cname']
        try:
            Equipment.objects.create(name=name,price=price,unit=unit,date=date,cname=cname)
            error='no'
        except:
            error='yes'
    context = {'error':error}    
    return render(request, 'gym/add_equipment.html',context)    

def view_equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    equ = Equipment.objects.all()
    context = {'equ':equ}    
    return render(request, 'gym/view_equipment.html',context)

def delete_equipment(request,id):
    if not request.user.is_staff:
        return redirect('login')
    equ = Equipment.objects.get(pk=id)
    equ.delete()
    return redirect('view_equipment')

#--start Plan code:-----------------------------------------------
def add_plan(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ''    
    if request.method == 'POST':
        name = request.POST['name']
        amount = request.POST['amount']    
        duration = request.POST['duration']        
        try:
            Plan.objects.create(name=name,amount=amount,duration=duration)
            error='no'
        except:
            error='yes'
    context = {'error':error}    
    return render(request, 'gym/add_plan.html',context)    

def view_plan(request):
    if not request.user.is_staff:
        return redirect('login')
    plans = Plan.objects.all()
    context = {'plans':plans}    
    return render(request, 'gym/view_plan.html',context)

def delete_plan(request,id):
    if not request.user.is_staff:
        return redirect('login')
    plan = Plan.objects.get(pk=id)
    plan.delete()
    return redirect('view_plan')

#--start Member code:-----------------------------------------------
def add_member(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ''    
    plan1 = Plan.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']        
        contact = request.POST['contact'] 
        age = request.POST['age']       
        gender = request.POST['gender']        
        p = request.POST['plan']        
        photo = request.FILES['photo']        
        joindate = request.POST['joindate']        
        expiredate = request.POST['expiredate']        
        initialamount = request.POST['initialamount']

        plan = Plan.objects.filter(name=p).first() 
        print(name,email,photo)       
        try:
            Member.objects.create(name=name,email=email,contact=contact,age=age,gender=gender,plan=plan,photo=photo,joindate=joindate,expiredate=expiredate,initialamount=initialamount)
            error='no'
        except:
            error='yes'
    context = {'error':error,'plans':plan1}    
    return render(request, 'gym/add_member.html',context)    

def view_member(request):
    if not request.user.is_staff:
        return redirect('login')
    member = Member.objects.all()
    context = {'mem':member}    
    return render(request, 'gym/view_member.html',context)

def delete_member(request,id):
    if not request.user.is_staff:
        return redirect('login')
    mem = Member.objects.get(pk=id)
    mem.delete()
    return redirect('view_member')