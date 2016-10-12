from django.db import IntegrityError
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

def publishers(request, orderby='pub_id'):
    if orderby=='pub_id': 
        idsort='-pub_id'
        namesort='name'
    elif orderby=='-pub_id':
        idsort='pub_id'
        namesort='name'
    elif orderby=='name':
        idsort='pub_id'
        namesort='-name'
    elif orderby=='-name':
        idsort='pub_id'
        namesort='name'

    pub_list = Publishers.objects.order_by(orderby)[:]
    context = {'pub_list': pub_list,'idsort':idsort,'namesort':namesort}
    return render(request, 'books/publishers.html', context)

def addpub(request):
    return HttpResponse("Add an publisher")

def updatepub(request,pub_id):
    pub = Publishers.objects.get(pub_id=pub_id)
    newtext = request.GET.get("newtext")
    pub.name = newtext
    pub.save()
    return HttpResponse("Modify an publisher" +newtext)

def deletepub(request, pub_id):
    pub = Publishers.objects.get(pub_id=pub_id)
    try:
        pub.delete()
        return HttpResponse(pub.name + " deleted successfully.")
    except IntegrityError as e:
        return HttpResponse(pub.name + " could not be deleted due to a referential integrity error.", status=403)
        




