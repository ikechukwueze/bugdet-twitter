from django.urls import path
from . import views



urlpatterns = [
    path('<str:username>/follow/', views.FollowUserView.as_view(), name='follow'),
    path('<str:username>/unfollow/', views.UnfollowUserView.as_view(), name='unfollow'),
    path('<str:username>/followers/', views.UserFollowersListView.as_view(), name='list-followers'),
    path('<str:username>/following/', views.UserFollowingListView.as_view(), name='list-following'),
    path('<str:username>/follower-count/', views.UserFollowerCountView.as_view(), name='list-followers'),
    path('<str:username>/following-count/', views.UserFollowingCountView.as_view(), name='list-following'),
]



