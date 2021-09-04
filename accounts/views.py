from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.conf import settings
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.urls import reverse
import jdatetime
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth.password_validation import validate_password, MinimumLengthValidator
from django.contrib.auth import authenticate, login
import random
from django.conf import settings

#handmade
from accounts.decorators import superuser_required
from accounts.models import UserModel
from accounts.forms import PasswordChangeForm, ForgotPasswordForm

# Create your views here.
@login_required
@superuser_required
def SuperUserDashboardView(request, slug):
    user = UserModel.objects.get(slug=slug)
    return render(request,'accounts/superuserdashboard.html')



@login_required
def PasswordChangeView(request,slug):
    user = get_object_or_404(UserModel,slug = slug)
    if request.method == 'POST':
        password_form = PasswordChangeForm(data = request.POST)
        if password_form.is_valid():
            current_password = password_form.cleaned_data.get('current_password')
            logged_in = authenticate(request, username=user.username, password=current_password)

            if logged_in is not None:
                if password_form.cleaned_data.get('new_password') == password_form.cleaned_data.get('confirm_password'):
                    new_password = password_form.cleaned_data.get('new_password')
                    try:
                        validate_password(new_password,user=user, password_validators=None)
                        user.set_password(new_password)
                        user.save()
                        return HttpResponseRedirect(reverse('accounts:login'))
                    except:
                        error1 ='کلمه عبور باید بیش از 6 کاراکتر باشد'
                        error2 ='کلمه عبور باید نمیتواند شامل نام کاربری باشد'
                        error3 ='کلمه عبور نمیتواند خیلی ساده باشد'
                        return render(request,'accounts/passwordchange.html',{'form':password_form,'error1':error1,'error2':error2,'error3':error3})
                else:
                    error4 = 'رمز های وارد شده با هم مطابقت ندارند'
                    password_form = PasswordChangeForm()
                    return  render(request,'accounts/passwordchange.html',
                                          {'error4':error4,'form':password_form})

            else:
                error4 = 'رمزعبور وارد شده صحیح نیست'
                password_form = PasswordChangeForm()
                return  render(request,'accounts/passwordchange.html',
                                      {'error4':error4,'form':password_form})
    else:
        password_form = PasswordChangeForm()
        return  render(request,'accounts/passwordchange.html',
                              {'form':password_form})




def ForgotPasswordView(request):
    #api = KavenegarAPI(settings.KAVENEGAR_API_KEY)
    try:
        last_retry_str = request.session['last_retry']
        last_retry = datetime.datetime.strptime(last_retry_str,"%Y-%m-%d %H:%M:%S")
    except:
        last_retry = datetime.datetime.now()
    now = datetime.datetime.now()
    if now >= last_retry:
        if request.method == 'POST':
            data = request.POST.copy()
            form = ForgotPasswordForm(data=request.POST)

            phone_number_exists = False
            if form.is_valid():
                phone_number = form.cleaned_data.get('phone_number')

                try :
                    user = get_object_or_404(UserModel,username = phone_number)
                    if user :
                        var = 'abcdefghijklmnpqrstuvwxyzABCDEFIJKLMNPQRSTUVWXYZ123456789'
                        new_password=''
                        for i in range(0,random.randrange(10,13,1)):
                            c = random.choice(var)
                            new_password += c

                            '''
                        params = {
                        'sender': settings.KAVENEGAR_PHONE_NUMBER,
                        'receptor': phone_number,
                        'message' : 'سامانه ورزش کن\n' + str(user.username) + ' :'+'نام کاربری شما'+'\n'+ new_password +' :'+ 'رمز عبور جدید شما '
                        }'''
                        #response = api.sms_send(params)
                        phone_number_exists = True
                        user.set_password(new_password)
                        print(new_password)
                        user.save()
                        now = datetime.datetime.now() + datetime.timedelta(minutes=3)
                        str_now = str(now.year)+'-'+str(now.month)+'-'+str(now.day)+' '+str(now.hour)+':'+str(now.minute)+':'+str(now.second)
                        request.session['last_retry'] = str_now
                        return HttpResponseRedirect(reverse('accounts:login'))
                except:
                    pass



            else:
                print(form.errors)
            if not phone_number_exists:
                return HttpResponseRedirect(reverse('accounts:wrongphonenumber'))


        else:
            form = ForgotPasswordForm()
        return render(request,'accounts/forgotpassword.html',{'form':form})
    else:
        return HttpResponseRedirect(reverse('accounts:wait'))


def WaitView(request):
    return render(request,'accounts/wait.html')


def WrongPhoneNumberView(request):
    return render(request,'accounts/wrongphonenumber.html')
