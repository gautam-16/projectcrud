from django.http import HttpResponse
from django.shortcuts import render, redirect
from CRUD.models import Employee


def index(request):
    return render(request, "CRUD/index.html")


def create(request, ):
    if request.method == 'POST':
        var = request.POST.get('a')
        var1 = request.POST.get('b')
        employee = Employee.objects.create(emp_id=var, emp_contact=var1)
        # employee.emp_id=var
        # employee.emp_contact=var1
        # print(employee.emp_id)
        employee.save()
        return redirect("read")  # render(request,('CRUD/read.html',{"employees": Employee.objects.all()}))
    return render(request, 'CRUD/create.html')


# def create(request,):
#     if request.method=='POST':
#         var=request.POST.get('a')
#         var1=request.POST.get('b')
#         employee=Employee.objects.create(emp_id=var,emp_contact=var1)
#         employee.save()
#         return render(request, 'CRUD/create.html')
#     elif request.method=="Get":
#         return HttpResponse("Creation with get method is not possible")
#     return render(request,'CRUD/create.html')


def read(request):
    employees = Employee.objects.all()
    return render(request, 'CRUD/read.html', {'employees': employees})


def update(request):
    if request.method == "POST":
        var = request.POST.get('a')
        var1 = request.POST.get('b')
        var11=request.POST.get('c')
        var12=request.POST.get('d')
        employee = Employee.objects.get(emp_id=var, emp_contact=var1)
        if var11!='' and var12!='':
            employee.emp_id=var11
            employee.emp_contact=var12
            employee.save()
        elif var11!='' and var12=='':
            employee.emp_id=var11
            employee.save()
        elif var11=='' and var12!='':
            employee.emp_contact=var12
            employee.save()
    return render(request,'CRUD/update.html')


def delete(request):
    if request.method == 'POST':
        var = request.POST.get('a')
        var1 = request.POST.get("b")
        employee = Employee.objects.get(emp_id=var, emp_contact=var1)
        employee.delete()
        return redirect("read")
    return render(request, 'CRUD/delete.html')
