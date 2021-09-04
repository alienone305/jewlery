from django.urls import include, path
from commonuser.views import (TwoMinWaitView, CommonUserSignupView, UserConfirmView,
                            CustomerListView, JewlerListView, JewlerReqListView,
                            JewlerConfirmView, JewlerDenyView, CommonUserProfileView,
                            CommonUserUpdateView)

# handmade
app_name ='commonuser'
urlpatterns = [
    path('signup/',CommonUserSignupView, name='signup'),
    path('confirm/',UserConfirmView, name='confirm'),
    path('wait/',TwoMinWaitView, name='twominwait'),
    path('customerlist/',CustomerListView, name='customerlist'),
    path('jewlerlist/',JewlerListView, name='jewlerlist'),
    path('jewlerreqlist/',JewlerReqListView, name='jewlerreqlist'),
    path('jewler-confirm/<int:pk>',JewlerConfirmView, name='jewlerconfirm'),
    path('jewler-deny/<int:pk>',JewlerDenyView, name='jewlerdeny'),
    path('profile/<slug:slug>',CommonUserProfileView, name='profile'),
    path('update/<slug:slug>',CommonUserUpdateView, name='update'),
]
