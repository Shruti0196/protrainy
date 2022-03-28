from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .models import WorkDetails,Todo
from django.db.models import Q
# Create your views here.
from .forms import TodoForm,DetailsForm

# def showform(request):
#     form=TodoForm()
#     return render(request,'index.html',{'form':form})

def addform(request):
    form=TodoForm()
    if request.method=='POST':
        # print("Post:",request.POST)
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/details')
    if request.method=='GET':        
        return render(request,'index.html',{'form':form}) 

def adddetailsform(request):
    form=DetailsForm()
    if request.method=='POST':
        form=DetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addform')
    return render(request,'index.html',{'form':form})

def updateworkdetails(request,pk):
    # work=WorkDetails.objects.get(Q(WorkDetails__Work__Work=pk))
    # work=WorkDetails.objects.filter(Work=work1)
    # print(work)
    work=WorkDetails.objects.get(Work=pk)
    form=DetailsForm(instance=work)
    if request.method=='POST':
        form=DetailsForm(request.POST,instance=work)
        if form.is_valid():
            form.save()
            return redirect('/display')
    return render(request,'index.html',{'form':form})


def Display(request):
    Todo=WorkDetails.objects.all()
    # Todo2=Todo.objects.all()
    return render(request,'Display.html',{'Todo':Todo})

def deletework(request,pk):
        work=WorkDetails.objects.get(desc=pk)
        work.delete()
        return redirect('/display')
    
