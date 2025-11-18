from django.urls import path
from .views import *

urlpatterns = [
    path('stu/view/',student_view,name="stu-view"),
]
