from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(requests):
    return HttpResponse("Hello")

def test(requests):
    template = loader.get_template('index.html')
    return render(requests,'index.html',{})
    # return HttpResponse("This is test")

def tail(requests):
    return render(requests,'tail.html',{})

def dyn(request,id):
    try:
         id
    except type(id) is str:
        raise Http404("Wrong input")

    return render(request,'index.html',{'id':id})