from django.shortcuts import redirect, render
from .models import TaskModel
from .forms import TaskForm


def home(request):
    if request.method=='GET':
        all=TaskModel.objects.all()
    return render(request,'home.html',{'all':all})

def addtask(request):

    if request.method=='POST':
        form=TaskForm(data=request.POST)

        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form=TaskForm(initial={'host':request.user})

    return render(request,'addtask.html',{'form':form})

def edit(request,id):
    data=TaskModel.objects.get(id=id)
    if request.method=='POST':
        data.Title=request.POST['Title']
        data.Description=request.POST['Description']
        data.Due_date=request.POST['Due_date']
        data.priority=request.POST['priority']
        data.Status=request.POST['Status']
        data.save()
        return redirect('home')
    return render(request,'edit.html',{'datas':data})

def delete(request,id):
    data=TaskModel.objects.get(id=id)
    data.delete()
    return redirect('home')
