from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os

# Create your views here.

def first(request):
    return HttpResponse("WELCOME TO DJANGO")

def second(request):
    return HttpResponse("WELCOME AGAIN...")

def third(requst):
    return HttpResponse("<h1>welcome<h1>"
                        "<p>this is a paragraph</p")
def another(request):
    return HttpResponse("<center><h2><u>PYTHON</u></h2><center>"
                        "<p>This is a paragraph about python,Python is a high-level, gener"
                        "al-purpose programming language. Its design philosophy emphasizes code "
                        "readability with the use of significant indentation. Python is dynamically-type"
                        "d and garbage</p>")

def fourth(request):
    return render(request,'first.html')
def fifth(request):
    return render(request,'second.html')


def register(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['cpassword']
            if ps==cp:
                b=regmodel(name=nm,email=em,phone=ph,password=ps)
                b.save()
                return HttpResponse("registration success")
            else:
                return HttpResponse("incorrect password")
        else:
            return HttpResponse("registration failed")
    else:
        return render(request,'register.html')


def loginpage(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                if i.email==em and i.password==ps:
                    return HttpResponse("login success")
            else:
                    return HttpResponse("login failed")
    else:
        return render(request,'loginpage.html')


# for loop used to iterate each field and check match with registered name and phone

# name  address phone
# arya   abc    7777  #i
# anju   xyz    8888  #i

def employee(request):
    if request.method == 'POST':
        a = employeeform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            sr = a.cleaned_data['salary']
            em = a.cleaned_data['email']
            cn = a.cleaned_data['cname']
            dn = a.cleaned_data['dname']
            b = employeemodel(name=nm, salary=sr, email=em, cname=cn, dname=dn)
            b.save()
            return HttpResponse("Employee data added successfully...")

        else:
            return HttpResponse("Failed")
    else:
        return render(request, 'employee.html')

def check(request):
    if request.method=='POST':
        a=checkform(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            b = employeemodel.objects.all()
            for i in b:
                if i.name==nm and i.email==em:
                    return HttpResponse("Employee Found")
            else:
                return HttpResponse("Employee Not Found")
    else:
        return render(request, 'check.html')


def display(request):
    x=regmodel.objects.all()
    return render(request,'display.html',{'a':x})


def employdisplay(request):
    x=employeemodel.objects.all()
    return render(request,'employeedisplay.html',{'a':x})


# context passed. this employee template can access the key.so it can access all the data which stored in 'a'.
# so we can iterate data from a.
# display html page type like table.not form bcz we are not post datas we just display.


def fileupload(request):
    if(request.method=='POST'):
        a=fileform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['itemname']
            im=a.cleaned_data['image']
            b=filemodel(itemname=nm,image=im)
            b.save()
            return HttpResponse("file upload successfully...")
        else:
            return HttpResponse("file upload failed...")
    else:
        return render(request,'fileupload.html')


# there are post data and file data.

def card(request):
    if(request.method=='POST'):
        a=cardform(request.POST,request.FILES)
        if a.is_valid():
            nm=a.cleaned_data['name']
            pr=a.cleaned_data['price']
            im=a.cleaned_data['image']
            dp=a.cleaned_data['description']
            b=cardmodel(name=nm,price=pr,image=im,description=dp)
            b.save()
            return HttpResponse("New product added successfully...")
        else:
            return HttpResponse("upload failed")
    else:
        return render(request,'card.html')

# enc type have to decript to display

def filedisplay(request):
    a=filemodel.objects.all()
    li=[]
    name=[]
    id=[]
    for i in a:
        id1=i.id
        id.append(id1)
        img=i.image
        li.append(str(img).split('/')[-1])
        nm=i.itemname
        name.append(nm)
    mylist=zip(li,name,id)
    return render(request,'filedisplay.html',{'list':mylist})


def carddisplay(request):
    a=cardmodel.objects.all()
    li=[]
    name1=[]
    name2=[]
    name3=[]
    id=[]
    for i in a:
        img=i.image
        li.append(str(img).split('/')[-1])
        nm=i.name
        ds=i.description
        pr=i.price
        id1=i.id
        name1.append(nm)
        name2.append(ds)
        name3.append(pr)
        id.append(id1)
    mylist=zip(li,name1,name2,name3,id)
    return render(request,'carddisplay.html',{'list':mylist})

def edituser(request,id):
    a=regmodel.objects.get( id=id)
    if request.method=='POST':
        a.name=request.POST.get('name')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.password=request.POST.get('password')
        a.save()
        return redirect(display)
    return render(request,'edituser.html',{'a':a})



def deleteuser(request,id):
    a=regmodel.objects.get(id=id)
    a.delete()
    return redirect(display)


def employedit(request,id):
    a=employeemodel.objects.get(id=id)
    if request.method=='POST':
        a.name=request.POST.get('name')
        a.salary=request.POST.get('salary')
        a.email=request.POST.get('email')
        a.cname=request.POST.get('cname')
        a.dname=request.POST.get('dname')
        a.save()
        return redirect(employdisplay)
    return render(request,'employedit.html',{'a': a})

def employdelete(request,id):
    a=employeemodel.objects.get(id=id)
    a.delete()
    return redirect(employdisplay)

def editproduct(request,id):
    a=filemodel.objects.get(id=id)
    image=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.itemname=request.POST.get('itemname')
        a.save()
        return redirect(filedisplay)
    return render(request,'editproduct.html',{'a':a,'image':image})


def deleteproduct(request,id):
    a=filemodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(filedisplay)

def editcard(request,id):
    a = cardmodel.objects.get(id=id)
    image = str(a.image).split('/')[-1]
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(a.image) > 0:
                os.remove(a.image.path)
            a.image = request.FILES['image']
        a.name = request.POST.get('name')
        a.save()
        return redirect(carddisplay)
    return render(request,'editcard.html',{'a': a,'image': image})


def deletecard(request,id):
    a=cardmodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(carddisplay)



def index(request):
    return render(request, 'index.html')


def logo(request):
    return render( request,'logo.html')

def Registration(request):
    return render( request,'Registration.html')



def xamfile(request):
    if(request.method=='POST'):
        a=xamform(request.POST,request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['name']
            im = a.cleaned_data['image']
            c = xammodel(name=nm,image=im)
            c.save()
            return HttpResponse("file upload successfully...")
        else:
            return HttpResponse("file upload failed...")
    else:
        return render(request,'xamfile.html')

def xamdisplay(request):
    a=xammodel.objects.all()
    li=[]
    name=[]
    id=[]
    for i in a:
        img=a.image
        li.append(str(img).split('/')[-1])
        nm=a.name
        name.append(nm)
        id1=i.id
        id.append(id1)
    mylist=zip(li,name,id)
    return render(request,'xamdisplay.html',{'list':mylist})

def editxam(request,id):
    a=xammodel.objects.get(id=id)
    image=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)!=0:
            if len(a.image)>0:
                os.remove(a.image.path)
            a.image=request.POST.get['image']
        a.name=request.POST.get('name')
        a.save()
        return redirect(xamdisplay)
    return render(request,'xamedit.html',{'a':a,'image':image})

def deletexam(request,id):
    a=xammodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    a.delete()
    return redirect(xamdisplay)


































