from django.urls import path
from . import views



urlpatterns = [
    path("signup/", views.AccountSignUpView.as_view(), name="account_signup"),
    path("login/", views.AccountLoginView.as_view(), name="account_login"),
    # path("follow/", views.FollowAccountView.as_view(), name="follow_account"),
    # path("unfollow/", views.UnfollowAccountView.as_view(), name="unfollow_account"),
]