from django.db import IntegrityError
from django.db import models 
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

def pubshell(request):
    return render(request, 'books/pubshell.html')

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

    search = request.GET.get("search")
    if search is None:
        search=""
    pub_list = Publishers.objects.filter(name__contains=search).order_by(orderby)[:]
    context = {'pub_list': pub_list,'idsort':idsort,'namesort':namesort,'orderby':orderby}
    return render(request, 'books/publishers.html', context)

def addpub(request):
    newtext = request.GET.get("newtext")
    pub=Publishers(name=newtext)
    pub.save()
    return HttpResponse(str(pub.pub_id))

def updatepub(request,pub_id):
    pub = Publishers.objects.get(pub_id=pub_id)
    newtext = request.GET.get("newtext")
    pub.name = newtext
    pub.save()
    return HttpResponse("Publisher name chaged to " +newtext)

def deletepub(request, pub_id):
    pub = Publishers.objects.get(pub_id=pub_id)
    try:
        pub.delete()
        return HttpResponse(pub.name + " deleted successfully.")
    except IntegrityError as e:
        return HttpResponse(pub.name + " could not be deleted due to a referential integrity error.", status=403)
        




