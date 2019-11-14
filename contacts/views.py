from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from datetime import datetime
from django.core.mail import send_mail
# Create your views here.


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        contact_date = datetime.now()
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You already have made an inquiry about this listing!')
            else:
                contact1 = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=
                                   message, user_id=user_id, contact_date=contact_date)
                contact1.save()
                messages.success(request, 'Your request has been submitted, realtor will get back to you soon!')
                send_mail(
                    'Property Listing Inquiry',
                    'There has been inquiry for ' + listing + '.Sign in to admin panel for more info.',
                    'empyrealgamesindia@gmail.com',
                    [realtor_email, 'empyrealgamesindia@gmail.com'],
                    fail_silently=False
                )
        return redirect('/listings/'+listing_id)

    else:
        return


def message(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        message_ = request.POST['message']
        user_id = request.POST['user_id']
        contact_date = datetime.now()
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            messages.success(request, 'Your message has been sent!')
            send_mail(
                'New Message',
                'You have received a new message on previous inquiry on ' + listing +
                'by user ' + name + ' having user id ' + str(user_id) + ' the message is ' + message_,
                'empyrealgamesindia@gmail.com',
                [realtor_email, 'empyrealgamesindia@gmail.com'],
                fail_silently=False
            )
        return redirect('/accounts/dashboard' + listing_id)

    else:
        return

