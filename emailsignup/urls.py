from django.conf.urls import url, include
from allauth.account.views import ConfirmEmailView
from . import views
from .views import LoginAPI
urlpatterns = [
    # Override urls
    url(r'^registration/account-email-verification-sent/', views.null_view, name='account_email_verification_sent'),
    url(r'^registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),
    url(r'^complete/', views.complete_view, name='account_confirm_complete'),
    url("login/", LoginAPI.as_view()),

    url(r'', include('rest_auth.urls')),
    url('registration/', include('rest_auth.registration.urls'))
]