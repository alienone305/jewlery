from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import jdatetime
from django.conf import settings
from django.utils import timezone

#handmade
from order.models import OrderModel
from order.forms import OrderForm
from commonuser.models import CommonUserModel
from accounts.models import UserModel
from jewlery.models import JewleryModel, UnitModel
from commonuser.decorators import commonuser_required, jewler_required
from masteruser.decorators import masteruser_required


@login_required
@commonuser_required
def OrderingView(request, pk):

    jewlery = get_object_or_404(JewleryModel, pk=pk)
    commonuser = get_object_or_404(CommonUserModel,user=request.user)
    unit = UnitModel.objects.latest('jdatetime')
    ### Calculate Price
    sale_weight = (jewlery.weight + jewlery.weight * jewlery.sale_wage/100) * jewlery.karat / 750
    price = (unit.unit/4.3317) * sale_weight / 10000
    price = int(price) + 1
    price = price * 10000
    ###
    if request.method == 'POST':
        order_form = OrderForm(data = request.POST)
        if order_form.is_valid():
             order = order_form.save(commit = False)
             order.commonuser = commonuser
             order.jewlery = jewlery
             order.price = price
             order.sale_wage = jewlery.sale_wage
             order.unit = unit.unit
             order.save()
             return HttpResponseRedirect(reverse('order:success'))
        else:
             print(order_form.errors)

    else:
        order_form = OrderForm()
        order_form.fields['name'].widget.attrs['value'] = request.user.name
        order_form.fields['phone_number'].widget.attrs['value'] = request.user.username
        order_form.fields['numbers'].widget.attrs['value'] = 1
    return render(request,'order/ordering.html',
                          {'form':order_form,'jewlery':jewlery})


def OrderSuccessView(request):
    return render(request,'order/success.html')


@login_required
@masteruser_required
def OrderListForJewleryView(request, pk):
    jewlery = JewleryModel.objects.get(pk = pk)
    orders = OrderModel.objects.filter(jewlery = jewlery)
    return render (request,'order/listforjewlery.html',{'orders':orders})


@login_required
@commonuser_required
def OrderListForCommonUserView(request, slug):
    user = UserModel.objects.get(slug = slug)
    commonuser = CommonUserModel.objects.get(user = user)
    orders = OrderModel.objects.filter(commonuser = commonuser)
    return render (request,'order/listforcommonuser.html',{'orders':orders})


@login_required
@masteruser_required
def CheckedOrderListView(request):
    orders = OrderModel.objects.filter(is_checked = True)
    return render (request,'order/checkedlist.html',{'orders':orders})


@login_required
@masteruser_required
def UnCheckedOrderListView(request):
    orders = OrderModel.objects.filter(is_checked = False)
    return render (request,'order/uncheckedlist.html',{'orders':orders})


@login_required
@masteruser_required
def CheckOrderView(request, pk):
    order = OrderModel.objects.get(pk = pk)
    order.is_checked = True
    order.save()
    return HttpResponseRedirect(reverse('order:uncheckedlist'))


@login_required
@masteruser_required
def DeleteOrderView(request, pk):
    order = OrderModel.objects.get(pk = pk)
    order.delete()
    return HttpResponseRedirect(reverse('order:uncheckedlist'))


@login_required
@masteruser_required
def UnCheckOrderView(request, pk):
    order = OrderModel.objects.get(pk = pk)
    order.is_checked = False
    order.save()
    return HttpResponseRedirect(reverse('order:checkedlist'))


@login_required
@masteruser_required
def DeliverOrderView(request, pk):
    order = OrderModel.objects.get(pk = pk)
    order.is_delivered = True
    order.save()
    return HttpResponseRedirect(reverse('order:checkedlist'))


@login_required
@masteruser_required
def UnDeliverOrderView(request, pk):
    order = OrderModel.objects.get(pk = pk)
    order.is_delivered = False
    order.save()
    return HttpResponseRedirect(reverse('order:deliveredlist'))


@login_required
@masteruser_required
def DeliveredOrderListView(request):
    orders = OrderModel.objects.filter(is_delivered = True)
    return render (request,'order/deliveredlist.html',{'orders':orders})


@login_required
@jewler_required
def OrderUpdateView(request,pk):
    order = get_object_or_404(OrderModel, pk = pk)
    if order.commonuser == request.user.commonusers:
        order_update_form = OrderForm(request.POST or None, instance = order)
        if order_update_form.is_valid():
            order_update_form.save()
            order.save()
            return HttpResponseRedirect(reverse('order:listforcommonuser'))
        return render(request,'order/update.html',
                              {'form':order_update_form,
                              'order':order,})
