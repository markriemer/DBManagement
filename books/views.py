from django.db import IntegrityError
from django.db import models 
from django.shortcuts import render
from django.http import HttpResponse

from .models import Books, Authors, Publishers, Wrote

# Create your views here.


#For the moment, this just lists books.  Need to add authors.
def index(request):
    book_list = Books.objects.order_by('book_id')[:]
    wrote_list = Wrote.objects.order_by('book')[:]
    context = {'book_list': book_list,'wrote_list':wrote_list}
    resp = render(request, 'books/index.html', context)
    return resp

def addbook(request):
    return HttpResponse("Add a book")

def modifybook(request):
    return HttpResponse("Modify a book")

def deletebook(request):
    return HttpResponse("Delete a book")

def authshell(request):
    return render(request, 'books/authshell.html')

def authors(request, orderby='auth_id'):
    if orderby=='auth_id': 
        idsort='-auth_id'
        namesort='name'
    elif orderby=='-auth_id':
        idsort='auth_id'
        namesort='name'
    elif orderby=='name':
        idsort='auth_id'
        namesort='-name'
    elif orderby=='-name':
        idsort='auth_id'
        namesort='name'

    search = request.GET.get("search")
    if search is None:
        search=""
    auth_list = Authors.objects.filter(name__contains=search).order_by(orderby)[:]
    context = {'auth_list': auth_list,'idsort':idsort,'namesort':namesort,'orderby':orderby}
    return render(request, 'books/authors.html', context)

def addauth(request):
    newtext = request.GET.get("newtext")
    auth=Authors(name=newtext)
    auth.save()
    return HttpResponse(str(auth.auth_id))

def updateauth(request, auth_id):
    auth = Authors.objects.get(auth_id=auth_id)
    newtext = request.GET.get("newtext")
    auth.name = newtext
    auth.save()
    return HttpResponse("Author name chaged to " +newtext)

def deleteauth(request, auth_id):
    auth = Authors.objects.get(auth_id=auth_id)
    try:
        auth.delete()
        return HttpResponse(auth.name + " deleted successfully.")
    except IntegrityError as e:
        return HttpResponse(auth.name + " could not be deleted due to a referential integrity error.", status=403)

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
        




