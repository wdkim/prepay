from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404

from prepay.models import Listing, Category

def index(request):
    return render(request, 'prepay/home.html')

def about(request):
    return render(request, 'prepay/about.html')

'''
todo: 
refactor this to support browse by different criteria e.g. category
for now, created redundant browse_by_category
'''
def browse(request):
    all_listings = Listing.objects.all().order_by('-created_at')
    context = Context({
        'all_listings': all_listings,
    })
    return render(request, 'prepay/browse.html', context)

'''
Pretty sick how this:

select prepay_listing.name, prepay_product.name, prepay_category.name
from prepay_product, prepay_category, prepay_product_categories, prepay_listing
where prepay_product.id = prepay_product_categories.product_id
and prepay_product.id = prepay_listing.product_id
and prepay_category.id = prepay_product_categories.category_id
and prepay_category.id = 1

equals this:

Listing.objects.filter(product__category__exact=cat_id)

'''
def browse_category(request, category_id):
    category = Category.objects.filter(pk = category_id)
    listings_by_category = Listing.objects.filter(product__categories__exact=category_id)
    print 'category? ' + category[0].name
    context = Context({
        'category': category[0],
        'listings_by_category': listings_by_category,
    })
    return render(request, 'prepay/browse_category.html', context)

def listing_detail(request, listing_id):
    #return HttpResponse("You're looking at the detailed view of listing %s." % listing_id)
    listing = get_object_or_404(Listing, pk=listing_id)
    return render(request, 'prepay/detail.html', {'listing':listing})
