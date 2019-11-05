from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(isPublished=True)[:3]
    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    mvp = Realtor.objects.filter(is_mvp=True)[:1]
    realtors = Realtor.objects.all()

    if len(mvp) > 0:
        context = {
            'mvp': mvp[0],
            'realtors': realtors
        }
    else:
        context = {
            'realtors': realtors,
        }

    return render(request, 'pages/about.html', context)


