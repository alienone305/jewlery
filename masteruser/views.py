from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone
from django.conf import settings
from django.utils.decorators import method_decorator

#handmade
from accounts.decorators import superuser_required
from masteruser.decorators import masteruser_required
from accounts.models import UserModel
from masteruser.models import MasterUserModel
from accounts.forms import UserForm
from masteruser.forms import MasterUserForm

# Create your views here.

@login_required
@superuser_required
def MasterUserSignupView(request):
    if request.method == 'POST':

        user_form = UserForm(data = request.POST)
        masteruser_form = MasterUserForm(data = request.POST)

        if user_form.is_valid() and masteruser_form.is_valid():

             user = user_form.save()
             user.is_masteruser = True
             user.save()
             masteruser = masteruser_form.save(commit=False)
             masteruser.user = user
             masteruser.save()
             ###
             return HttpResponseRedirect(reverse('home'))
        else:
             print(user_form.errors,masteruser_form.errors)


    else:
        user_form = UserForm()
        masteruser_form = MasterUserForm()

    return render(request,'masteruser/signup.html',
                          {'user_form':user_form,
                           'masteruser_form':masteruser_form,})


@method_decorator([login_required, superuser_required], name='dispatch')
class MasterUserListView(ListView):
    model = MasterUserModel
    context_object_name = 'masterusers'
    template_name = 'masteruser/list.html'


@login_required
@superuser_required
def MasterUserDeleteView(request,slug):
    if request.user.is_superuser:
        user = get_object_or_404(UserModel,slug = slug)
        masteruser = get_object_or_404(MasterUserModel,user = user)
        masteruser.delete()
        user.delete()
        return HttpResponseRedirect(reverse('accounts:dashboard',kwargs={'slug':request.user.slug}))
    else:
        return HttpResponseRedirect(reverse('accounts:login'))


@login_required
@masteruser_required
def MasterUserDashboardView(request,slug):
    return render(request,'masteruser/dashboard.html')
