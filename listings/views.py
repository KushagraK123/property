from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from .models import Listing
from django.contrib import auth, messages
# Create your views here.


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(isPublished=True, isSold=False)
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    if request.user.is_authenticated:
        lis = get_object_or_404(Listing, pk=listing_id, isSold=False)
        realtor = lis.realtor
        context = {
            'listing': lis,
            'realtor': realtor,
        }
        return render(request, 'listings/listing.html', context)
    else:
        messages.error(request, 'Please Login to view listing!')
        return redirect('index')


def search(request):
    listings = Listing.objects.order_by('-list_date').filter(isPublished=True, isSold=False)
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)

