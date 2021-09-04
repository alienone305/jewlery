from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404

from .models import ContactUsModel
from .forms import ContactUsForm
from masteruser.decorators import masteruser_required



def AboutUsView(request):
    return render(request,'company/aboutus.html')


def FAQsView(request):
    return render(request,'company/faqs.html')


def TermandConditionsView(request):
    return render(request,'company/termsandconditions.html')


def ContactUsView(request):
    if request.method == 'POST':
        contactus_form = ContactUsForm(data = request.POST)
        if contactus_form.is_valid():
             contactus = contactus_form.save(commit=False)
             contactus.save()
             return HttpResponseRedirect(reverse('home'))
        else:
            print(contactus.errors)
    else:
        contactus_form = ContactUsForm()
    return render(request,'company/contactus.html',
                  {'form':contactus_form})


@login_required
@masteruser_required
def ContactUsListView(request):
    try:
        contactus_list = ContactUsModel.objects.order_by('created')
        return render(request,'company/contactuslist.html',
                      {'contactus_list':contactus_list})
    except:
        return render(request,'company/contactuslist.html')


@login_required
@masteruser_required
def ContactUsDeleteView(request, pk):
    contactus = get_object_or_404(ContactUsModel, pk = pk)
    contactus.delete()
    return HttpResponseRedirect(reverse('company:contact-us-list'))
