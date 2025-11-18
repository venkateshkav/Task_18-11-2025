from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.db.models import F, Q ,Count ,Max, Avg
from django.db.models import Sum,Max,Min,Count

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

def dashboard(request):
    query = request.GET.get("q", "")
    search_result = None
    if query:
        search_result = Book.objects.filter(author__icontains=query)
        available_books = Book.objects.filter(is_available=True)
        ordered_books = Book.objects.order_by("-price")
        category_count = Book.objects.values("category").annotate(total=Count("id"))
        avg_price = Book.objects.aggregate(Avg("price"))["price__avg"]
        total_books = Book.objects.count()
        latest_books = Book.objects.order_by("-published_date")[:5]
        context = {
            "search_result": search_result,
            "available_books": available_books,
            "ordered_books": ordered_books,
            "category_count": category_count,
            "avg_price": avg_price,
            "total_books": total_books,
            "latest_books": latest_books,
            "query": query
        }
        return render(request, "dashboard.html", context)

