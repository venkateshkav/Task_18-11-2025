from django.urls import path
from .views import *

urlpatterns = [
    path('book/',book_data,name="bok_create"),
    path('book/edit/<int:book_id>/',book_edit, name="bok_edit"),
    path('book/del/<int:book_id>/',book_delete, name="bok_del"),
]