from django.urls import include, path
from jewlery.views import (JewleryCreateView,ConfirmedJewleryListView, JewleryDetailView,
                            JewleryUpdateView, JewleryPictureUpdateView, JewleryPictureAddView,
                            UnConfirmedJewleryListView, JewleryPublicListView, JewleryDeleteView,
                            JewleryPublicDetailView, CreateUnitView)

app_name = 'jewlery'
urlpatterns = [
    path('create-unit/', CreateUnitView, name='createunit'),
    path('create/', JewleryCreateView, name='create'),
    path('confirmed-list/', ConfirmedJewleryListView, name='confirmedlist'),
    path('unconfirmed-list/', UnConfirmedJewleryListView, name='unconfirmedlist'),
    path('public-list/', JewleryPublicListView, name='publiclist'),
    path('public-detail/<int:pk>/', JewleryPublicDetailView, name='publicdetail'),
    path('detail/<int:pk>/', JewleryDetailView, name='detail'),
    path('update/<int:pk>/', JewleryUpdateView, name='update'),
    path('delete/<int:pk>/', JewleryDeleteView, name='delete'),
    path('picture-update/<int:pk>/', JewleryPictureUpdateView, name='pictureupdate'),
    path('picture-add/<int:pk>/', JewleryPictureAddView, name='pictureadd'),

]
