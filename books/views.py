from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Sortable/searchable listing of all books with authors/pubs.")

def addbook(request):
    return HttpResponse("Add a book")

def modifybook(request):
    return HttpResponse("Modify a book")

def deletebook(request)
    return HttpResponse("Delete a book")

def addauthor(request)
    return HttpResponse("Add an author")

def modifyauthor(request)
    return HttpResponse("Modify an author")

def deleteauthor(request)
    return HttpResponse("Delete an author")

def addpub(request)
    return HttpResponse("Add an publisher")

def modifypub(request)
    return HttpResponse("Modify an publisher")

def deletepub(request)
    return HttpResponse("Delete an publisher")




