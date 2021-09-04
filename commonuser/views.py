from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import jdatetime
import datetime
import random
from django.conf import settings
from django.utils import timezone

#handmade
from accounts.models import UserModel
from accounts.forms import UserForm, UserUpdateForm
from commonuser.models import CommonUserModel
from commonuser.forms import CommonUserForm, ConfirmationForm
from masteruser.decorators import masteruser_required
from commonuser.decorators import commonuser_required

# Create your views here.
def CommonUserSignupView(request):
    #api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    try:
        last_retry_str = request.session['last_retry']
        retries = request.session['retries']
        last_retry = datetime.datetime.strptime(last_retry_str,"%Y-%m-%d %H:%M:%S")
    except:
        last_retry = datetime.datetime.now()
    now = datetime.datetime.now()
    if now >= last_retry or retries != 2:
        if request.method == 'POST':

            user_form = UserForm(data = request.POST)
            commonuser_form = CommonUserForm(data = request.POST)

            if user_form.is_valid() and commonuser_form.is_valid():
                 request.session['name'] =  user_form.cleaned_data.get('name')
                 request.session['password1'] =  user_form.cleaned_data.get('password1')
                 request.session['username'] = user_form.cleaned_data.get('username')
                 request.session['address'] = commonuser_form.cleaned_data.get('address')
                 request.session['is_jewler_request'] = commonuser_form.cleaned_data.get('is_jewler_request')
                 #### generating code
                 var = '1234567890'
                 random_code=''
                 for i in range(5):
                     c = random.choice(var)
                     random_code += c
                 code = random_code
                 ######### send code to commonuser
                 '''
                 params = {
                 'sender': settings.KAVENEGAR_PHONE_NUMBER,
                 'receptor': phone_number,
                 'message' : 'سامانه ورزش کن \n' +'کد فعالسازی شما' +  ' :' + code
                 }
                 '''
                 try:
                     #response = api.sms_send(params)
                     print(code)
                     request.session['code'] =  code
                     now = datetime.datetime.now() + datetime.timedelta(minutes=2)
                     str_now = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                     request.session['last_retry'] = str_now
                     try:
                         if request.session['retries'] == 1:
                             request.session['retries'] = 2
                     except:
                         request.session['retries'] = 1


                 except:
                     return HttpResponseRedirect(reverse('accounts:wrongphonenumber'))


                 return HttpResponseRedirect(reverse('commonuser:confirm'))
            else:
                print(user_form.errors,commonuser_form.errors)


        else:
            user_form = UserForm()
            commonuser_form = CommonUserForm()

        return render(request,'commonuser/signup.html',
                              {'user_form':user_form,
                               'commonuser_form':commonuser_form})
    else:
        return HttpResponseRedirect(reverse('commonuser:twominwait'))



def UserConfirmView(request):
    name = request.session['name']
    password1 = request.session['password1']
    username = request.session['username']
    address = request.session['address']
    code = request.session['code']
    is_jewler_request = request.session['is_jewler_request']
    if is_jewler_request:
        is_jewler_request = True
    else:
        is_jewler_request = False
    if request.method == 'POST':

        confirmation_form = ConfirmationForm(data = request.POST)

        if confirmation_form.is_valid():
            confirmation_code = confirmation_form.cleaned_data.get('code')
            if confirmation_code == code:
                user = UserModel.objects.create(username=username, password=password1,
                                            name = name)
                user.is_active = True
                user.is_commonuser = True
                # hashing password
                user.set_password(user.password)
                user.save()
                print(address,'2')
                commonuser = CommonUserModel.objects.create(user=user, address=address, is_jewler_request = is_jewler_request)
                commonuser.save()
                return HttpResponseRedirect(reverse('accounts:login'))
        else:
            print(confirmation_form.errors)


    else:
        confirmation_form = ConfirmationForm()
    return render(request,'commonuser/confirm.html',
                          {'confirmation_form':confirmation_form,'phone_number':username})
#    except:
#        return HttpResponseRedirect(reverse('commonuser:signup'))


def TwoMinWaitView(request):
    return render(request,'accounts/wait.html')

@login_required
@masteruser_required
def CustomerListView(request):
    customers = CommonUserModel.objects.filter(is_jewler_request = False)
    return render (request,'commonuser/customerlist.html',{'customers':customers})


@login_required
@masteruser_required
def JewlerReqListView(request):
    jewlers = CommonUserModel.objects.filter(is_jewler_request = True, is_jewler = False)
    return render (request,'commonuser/jewlerreq.html',{'jewlers':jewlers})


@login_required
@masteruser_required
def JewlerListView(request):
    jewlers = CommonUserModel.objects.filter(is_jewler = True)
    return render (request,'commonuser/jewlers.html',{'jewlers':jewlers})


@login_required
@masteruser_required
def JewlerConfirmView(request,pk):
    jewler = get_object_or_404(CommonUserModel,pk=pk)
    jewler.is_jewler = True
    jewler.is_jewler_request = False
    jewler.save()
    return HttpResponseRedirect(reverse('commonuser:jewlerreqlist'))


@login_required
@masteruser_required
def JewlerDenyView(request,pk):
    jewler = get_object_or_404(CommonUserModel,pk=pk)
    jewler.is_jewler_request = False
    jewler.save()
    return HttpResponseRedirect(reverse('commonuser:jewlerreqlist'))


@login_required
@commonuser_required
def CommonUserProfileView(request,slug):
    commonuser_user = get_object_or_404(UserModel,slug=slug)
    commonuser = get_object_or_404(CommonUserModel,user=commonuser_user)
    return render (request,'commonuser/profile.html',{'commonuser':commonuser})


@login_required
@commonuser_required
def CommonUserUpdateView(request,slug):
    commonuser_user = get_object_or_404(UserModel,slug = slug)
    commonuser = get_object_or_404(CommonUserModel,user=commonuser_user)
    if request.user == commonuser_user :
        user_update_form = UserUpdateForm(request.POST or None, instance = commonuser_user)
        commonuser_update_form = CommonUserForm(request.POST or None, instance = commonuser)
        if user_update_form.is_valid() and commonuser_update_form.is_valid():
            user_update_form.save()
            commonuser_update_form.save()
            return HttpResponseRedirect(reverse('commonuser:profile',
                                        kwargs={'slug':commonuser_user.slug}))
        return render(request,'commonuser/update.html',
                              {'user_form':user_update_form,'commonuser_form':commonuser_update_form})
    else:
        return HttpResponseRedirect(reverse('accounts:login'))
