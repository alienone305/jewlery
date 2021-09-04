from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.utils import timezone
from django.conf import settings
import jdatetime
import datetime
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator

#handmade
from jewlery.models import JewleryModel, JewleryPictureModel, UnitModel
from jewlery.forms import JewleryForm, JewleryPictureForm, JewleryPictureUpdateForm, UnitForm
from masteruser.decorators import masteruser_required
from jewlery.filters import JewleryFilter
from jewlery.utils import Scraping, UpdatePrice


@login_required
@masteruser_required
def JewleryCreateView(request):
    imageformset = modelformset_factory(JewleryPictureModel,
                                        form=JewleryPictureForm, extra=10)
    if request.method == 'POST':
        jewlery_form = JewleryForm(data = request.POST)
        formsets = imageformset(request.POST or None, request.FILES or None)

        if jewlery_form.is_valid() and formsets.is_valid():
             jewlery = jewlery_form.save()
             formsets = imageformset(request.POST or None, request.FILES or None)
             jewlery.save()
             for formset in formsets.cleaned_data:
                    if formset:
                        picture = formset['picture']
                        photo = JewleryPictureModel(jewlery = jewlery, picture = picture)
                        photo.save()
             return HttpResponseRedirect(reverse('masteruser:dashboard',kwargs={'slug':request.user.slug}))
        else:
             print(jewlery_form.errors)


    else:
        jewlery_form = JewleryForm()
        formsets = imageformset(queryset=JewleryPictureModel.objects.none())
    return render(request,'jewlery/create.html',
                          {'form':jewlery_form,'formsets':formsets})


@login_required
@masteruser_required
def ConfirmedJewleryListView(request):
    jewleries = JewleryModel.objects.filter(is_confirmed = True)
    jewlery_filter = JewleryFilter(request.GET,queryset = jewleries)
    paginator = Paginator(jewlery_filter.qs, 10)
    page = request.GET.get('page')
    jewlery_list = paginator.get_page(page)
    return render (request,'jewlery/confirmedlist.html',{'jewleries':jewlery_list,'filter':jewlery_filter})



@login_required
@masteruser_required
def UnConfirmedJewleryListView(request):
    jewleries = JewleryModel.objects.filter(is_confirmed = False)
    return render (request,'jewlery/unconfirmedlist.html',{'jewleries':jewleries})


@login_required
@masteruser_required
def JewleryDetailView(request, pk):
    jewlery = JewleryModel.objects.get(pk = pk)
    jewleries = JewleryModel.objects.filter(is_confirmed = False)
    return render (request,'jewlery/detail.html',{'jewlery':jewlery,'jewleries':jewleries})


def JewleryPublicListView(request):
    Scraping()
    UpdatePrice(request)
    jewleries = JewleryModel.objects.filter(is_confirmed = True)
    jewlery_filter = JewleryFilter(request.GET,queryset = jewleries)
    paginator = Paginator(jewlery_filter.qs, 10)
    page = request.GET.get('page')
    jewlery_list = paginator.get_page(page)
    return render (request,'jewlery/publiclist.html',{'jewleries':jewlery_list,'filter':jewlery_filter})


def JewleryPublicDetailView(request, pk):
    Scraping()
    UpdatePrice(request)
    jewlery = JewleryModel.objects.get(pk = pk)
    jewleries = JewleryModel.objects.all()
    return render (request,'jewlery/publicdetail.html',{'jewlery_detail':jewlery,'jewleries':jewleries})


@login_required
@masteruser_required
def JewleryUpdateView(request,pk):
    jewlery = get_object_or_404(JewleryModel, pk = pk)

    jewlery_update_form = JewleryForm(request.POST or None, instance = jewlery)
    if jewlery_update_form.is_valid():
        jewlery_update_form.save()
        jewlery.save()
        return HttpResponseRedirect(reverse('jewlery:detail',
                                    kwargs={'pk':jewlery.pk,}))
    return render(request,'jewlery/update.html',
                          {'form':jewlery_update_form,
                          'jewlery':jewlery,})

@login_required
@masteruser_required
def JewleryPictureUpdateView(request, pk):
    pic = JewleryPictureModel.objects.get(pk=pk)
    form = JewleryPictureUpdateForm(request.POST or None,instance=pic)
    if form.is_valid():
        form.save()
        if 'picture' in request.FILES:
            pic.picture = request.FILES['picture']

        pic.save()
        return HttpResponseRedirect(reverse('jewlery:update',
                                    kwargs={'pk':pic.jewlery.pk}))
    else:
        print(form.errors)
        return render(request, 'jewlery/pictureupdate.html', {'form':form})


@login_required
@masteruser_required
def JewleryPictureAddView(request, pk):
    jewlery = JewleryModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = JewleryPictureForm(data = request.POST)
        if form.is_valid():
            pic = form.save(commit = False)
            pic.jewlery = jewlery
            if 'picture' in request.FILES:
                pic.picture = request.FILES['picture']
            pic.save()
        return HttpResponseRedirect(reverse('jewlery:update',
                                    kwargs={'pk':pic.jewlery.pk}))
    else:
        form = JewleryPictureForm()
    return render(request, 'jewlery/pictureadd.html', {'form':form})


@login_required
@masteruser_required
def JewleryDeleteView(request, pk):
    jewlery = JewleryModel.objects.get(pk=pk)
    jewlery.delete()
    return HttpResponseRedirect(reverse('masteruser:dashboard',kwargs={'slug':request.user.slug}))


@login_required
@masteruser_required
def CreateUnitView(request):
    if request.method == 'POST':
        unit_form = UnitForm(data = request.POST)
        if unit_form.is_valid():
             unit = unit_form.save(commit=False)
             unit.unit_gram = unit.unit/4.3317
             unit.save()
             return HttpResponseRedirect(reverse('masteruser:dashboard',kwargs={'slug':request.user.slug}))
        else:
            print(unit_form.errors)
    else:
        unit_form = UnitForm()
    return render(request,'jewlery/createunit.html',
                  {'form':unit_form})
