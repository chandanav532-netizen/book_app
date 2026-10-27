from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import book
from .serializer import bookserializer
@api_view(['GET','POST'])
def book_list(request):
    """
    GET
    return list of all books
    POST it creates a new book
    """
    if  request.method=='GET':
        books=book.objects.all()
        serializer=bookserializer(books,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
