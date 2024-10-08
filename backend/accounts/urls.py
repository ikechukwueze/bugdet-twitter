from django.urls import path
from . import views



urlpatterns = [
    path("signup/", views.AccountSignUpView.as_view(), name="account_signup"),
    path("login/", views.AccountLoginView.as_view(), name="account_login"),
    path("<str:username>/detail/", views.RetrieveUserDetailView.as_view(), name='account-detail')
]