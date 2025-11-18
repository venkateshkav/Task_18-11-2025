from django.shortcuts import render
from .models import *
from django.db.models import F,Q
from django.db.models import Sum,Max,Min,Count

# Create your views here.
def student_view(request):
    data = Student.objects.all()
    specific_dept = Student.objects.filter(department="IT")
    more_than_80 = Student.objects.filter(marks__gt = 80)
    less_than_75 = Student.objects.filter(marks__lt = 75)
    unique_dept = Student.objects.values_list("department",flat=True).distinct()
    sa_or_co = Student.objects.filter(Q(city="salem") | Q(city = "coimbatore"))
    add = Student.objects.update(attendence = F('attendence')+5)
    att = Student.objects.filter(attendence=0).delete()
    mak = Student.objects.filter(fees_paid = F('marks')*100)
    stu = Student.objects.filter(year = 3)
    all = Student.objects.values('name','mentor')

    return render(request,"student.html",{"data":data,"specific_dept":specific_dept,"more_than_80":more_than_80,"less_than_75":less_than_75,"unique_dept":unique_dept,"sa_or_co":sa_or_co,"add":add,"att":att,"mak":mak,"stu":stu,"all":all})