from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from myapp.models import *
def show_about_page(request):
    name="rajeev"
    link="techiu.epizy.com"
    data={
        'name':name,
        'link':link
    }
    return render(request,"about.html",data)
    
def show_home_page(request):
    images=Image.objects.all()
    cats=Category.objects.all()
    
    data={
        'images':images,
        "cats":cats
    }
    return render(request ,'home.html',data)    
def show_category_page(request,cid):
    print(cid)
    cats=Category.objects.all()
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    
    data={
        'images':images,
        "cats":cats
    }
    return render(request ,'home.html',data)    

def home(request):
    return redirect('/home')
