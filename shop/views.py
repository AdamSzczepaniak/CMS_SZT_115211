from django.shortcuts import render
from django.http import HttpResponse

def product_detail(request, product_id):
    return HttpResponse("You're looking at question %s." % product_id)
