from django.urls import include, path
from masteruser.views import (MasterUserSignupView, MasterUserListView,
                            MasterUserDeleteView, MasterUserDashboardView)

app_name = 'masteruser'
urlpatterns = [
    path('signup/', MasterUserSignupView, name='signup'),
    path('list/', MasterUserListView.as_view(), name='list'),
    path('delete/<slug:slug>', MasterUserDeleteView, name='delete'),
    path('dashboard/<slug:slug>', MasterUserDashboardView, name='dashboard'),


]
