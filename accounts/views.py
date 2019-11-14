from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from .models import Otp
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.utils import timezone
from random import randint


def login(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        user = None
        if user_type == 'realtor':
            user = auth.authenticate(username=username, password=password)
            if user.groups.filter(name='realtor').exists():
                pass
            else:
                user = None
        else:
            user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    elif request.method == 'GET':
        user_type = request.GET.get('user_type', 'user')
        context = {
            'user_type': user_type
        }
        return render(request, 'accounts/login.html', context)
    else:
        return


def dashboard(request):
    if auth.user_logged_in:
        user_contacts = Contact.objects.all().order_by('-contact_date').filter(user_id=request.user.id)
        context = {
            'contacts': user_contacts
        }
        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('index')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        user_type = request.POST['user_type']
        if password == password2:
            if User.objects.all().filter(username=username).exists():
                messages.error(request, 'User Name is Taken!')
                return redirect('register')
            else:
                if User.objects.all().filter(email=email).exists():
                    messages.error(request, 'Email is already in use!')
                    return redirect('register')
                else:
                    # user = User.objects.create_user(username=username, password=password, email=email,
                    #                              first_name=first_name, last_name=last_name)
                    otp = randint(100000, 999999)

                    context = {
                        'username': username,
                        'password': password,
                        'email': email,
                        'first_name': first_name,
                        'last_name': last_name,
                        'user_type': user_type,
                    }
                    obj = Otp.objects.all().filter(email=email )
                    if obj.exists():
                        obj = obj[0]
                        obj.otp = otp
                        obj.save()
                    else:
                        obje = Otp(email=email, otp=otp, time=timezone.now())
                        obje.save()
                    send_mail(
                        'Verify your email address',
                        'Your otp for real estate is ' + str(otp) + ', kindly confirm your email address!',
                        'empyrealgamesindia@gmail.com',
                        [email],
                        fail_silently=False
                    )


                    # messages.success(request, 'Successfully created new user!')
                    # user.save()
                    return render(request, 'accounts/verify_email.html', context)
        else:
            messages.error(request, 'Passwords do not Match!')
            return redirect('register')

    else:
        user_type = request.GET.get('user_type', 'user')
        context = {
            'user_type': user_type
        }
        return render(request, 'accounts/register.html', context)


def change_password(request):
    if request.method == 'POST':
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_id = request.POST['user_id']
        username = User.objects.get(id=user_id)
        print(username)
        if password2 == password1:
            user = User.objects.get(username__exact=username)
            user.set_password(password1)
            user.save()
            messages.success(request, 'Successfully changed password, Please login again!')
        else:
            messages.error(request, 'Passwords do not match!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def verify_otp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['user_type']
        obj = Otp.objects.all().filter(email=email)
        obj = obj[0]

        otp = obj.otp
        print('otp = ' + str(otp))
        otp2 = request.POST['otp2']
        if str(otp) == str(otp2):
            user = User.objects.create_user(username=username, password=password, email=email,
                                            first_name=first_name, last_name=last_name)
            if user_type == 'realtor':
                group = Group.objects.get(name='realtor')
                user.groups.add(group)
                user.is_staff = True
            user.save()
            messages.success(request, 'You have been registered successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Incorrect OTP, Please try again!')
            context = {
                'username': username,
                'password': password,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'otp': otp
            }
            return render(request, 'accounts/verify_email.html', context)
    return HttpResponseBadRequest()


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
    else:
        return redirect('index')


