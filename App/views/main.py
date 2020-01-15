from django.shortcuts import render,HttpResponse

def index(req):
    return HttpResponse('你好 Django')

def yankee(req):
    return HttpResponse('你好 Yankee')

# Create your views here.
