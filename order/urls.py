from django.urls import include, path
from order.views import (OrderingView,OrderSuccessView, OrderListForJewleryView,
                        CheckedOrderListView, UnCheckedOrderListView, OrderListForCommonUserView,
                        CheckOrderView, UnCheckOrderView, OrderUpdateView, DeliverOrderView,
                        DeliveredOrderListView, UnDeliverOrderView, DeleteOrderView)

app_name = 'order'
urlpatterns = [
    path('ordering/<int:pk>/', OrderingView, name='ordering'),
    path('update/<int:pk>/', OrderUpdateView, name='update'),
    path('success/', OrderSuccessView, name='success'),
    path('list-for-jewlery/<int:pk>', OrderListForJewleryView, name='listforjewlery'),
    path('list-for-user/<slug:slug>', OrderListForCommonUserView, name='listforuser'),
    path('checked-list/', CheckedOrderListView, name='checkedlist'),
    path('unchecked-list/', UnCheckedOrderListView, name='uncheckedlist'),
    path('check/<int:pk>/', CheckOrderView, name='check'),
    path('uncheck/<int:pk>/', UnCheckOrderView, name='uncheck'),
    path('deliver/<int:pk>/', DeliverOrderView, name='deliver'),
    path('deliver/<int:pk>/', DeleteOrderView, name='delete'),
    path('undeliver/<int:pk>/', UnDeliverOrderView, name='undeliver'),
    path('delivered-list/', DeliveredOrderListView, name='deliveredlist'),


]
