from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from prepay.models import Listing

def index(request):
    return render(request, 'prepay/home.html')

def about(request):
    return render(request, 'prepay/about.html')

def browse(request):

    all_listings = Listing.objects.all().order_by('-created_at')
    #template = loader.get_template('myILS/browse.html')
    context = Context({
        'all_listings': all_listings,
    })
    
    return render(request, 'prepay/browse.html', context)

def listing_detail(request, listing_id):
    #return HttpResponse("You're looking at the detailed view of listing %s." % listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'prepay/detail.html', {'listing':listing})