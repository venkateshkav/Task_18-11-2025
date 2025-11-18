from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *

# Create your views here.
def book_data(request):
    form = BookForm()
    data = Book.objects.all()
    if request.method =="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("Error")
    return render(request,"book.html",{"data":data,"form":form}) 

def book_edit(request,book_id):
    data = Book.objects.get(id=book_id)
    form = BookForm(instance=data)
    if request.method == "POST":
        form = BookForm(instance=data,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bok_create")
        else:
            return HttpResponse("Error")
        
    return render(request,"book_edit.html",{"form":form})

def book_delete(request,book_id):
    data = Book.objects.get(id=book_id)
    data.delete()
    return redirect("bok_create")
