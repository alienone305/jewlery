from django.urls import include, path
from django.contrib.auth import views as auth_views
from accounts.forms import UserLoginForm
from accounts.views import (SuperUserDashboardView, PasswordChangeView,
                        ForgotPasswordView, WaitView, WrongPhoneNumberView)

# handmade
app_name ='accounts'
urlpatterns = [
    path('auth/',auth_views.LoginView.as_view(template_name='registration/login.html',authentication_form=UserLoginForm), name='login'),
    path('dashboard/<slug:slug>/',SuperUserDashboardView, name='dashboard'),
    path('wait/',WaitView, name='wait'),
    path('wrongphonenumber/',WrongPhoneNumberView, name='wrongphonenumber'),
    path('password-change/<slug:slug>/',PasswordChangeView, name='passwordchange'),
    path('password-forget/',ForgotPasswordView, name='passwordforget'),
]
