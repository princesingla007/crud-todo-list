from django.shortcuts import render,redirect
from . models import Employee

# Create your views here.
def index(request):
    data=Employee.objects.all()
    context={'data':data}
    return render(request,"index.html",context)

def insert(request):
    if request.method=="POST":
        name=request.POST.get("name")
        emp=request.POST.get("emp")
        add=request.POST.get("add")
        gender=request.POST.get("gender")

        query=Employee(name=name,emp=emp,add=add,gender=gender)
        query.save()
        return redirect("/")
    
    return render(request,"index.html")

def update(request,id):
    if request.method=="POST":
        name=request.POST.get("name")
        emp=request.POST.get("emp")
        add=request.POST.get("add")
        gender=request.POST.get("gender")
        edit=Employee.objects.get(id=id)
        edit.name=name
        edit.emp=emp
        edit.add=add
        edit.gender=gender
        edit.save()
        return redirect("/")
    d=Employee.objects.get(id=id)
    context={'d':d}


    return render(request,"edit.html",context)

def delete(request,id):
    d=Employee.objects.get(id=id)
    d.delete()
    return redirect("/")
