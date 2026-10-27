from .views import book_list
from django.urls import path,include

urlpatterns = [
    path('books/',book_list,name='book-list')
]
