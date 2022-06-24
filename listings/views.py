from multiprocessing import context
from django.shortcuts import render
from .models import Listing
# Create your views here.

def listings(request):
    listings = Listing.objects.all()
    context = {
        'listings':listings
    }
    return render(request,'listings.html',context)

def listing(request,id):
    listing = Listing.objects.get(id=id)
    context = {
        'listing':listing
    }
    return render(request,'listing.html',context)

