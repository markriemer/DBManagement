from django.shortcuts import render
from django.http import HttpResponse

from .models import Books, Authors, Publishers

# Create your views here.


#For the moment, this just lists books.  Need to add authors.
def index(request):
    book_list = Books.objects.order_by('book_id')[:]
    context = {'book_list': book_list}
    return render(request, 'books/index.html', context)

def addbook(request):
    return HttpResponse("Add a book")

def modifybook(request):
    return HttpResponse("Modify a book")

def deletebook(request):
    return HttpResponse("Delete a book")

def addauthor(request):
    return HttpResponse("Add an author")

def modifyauthor(request):
    return HttpResponse("Modify an author")

def deleteauthor(request):
    return HttpResponse("Delete an author")

def addpub(request):
    return HttpResponse("Add an publisher")

def modifypub(request):
    return HttpResponse("Modify an publisher")

def deletepub(request):
    return HttpResponse("Delete an publisher")




