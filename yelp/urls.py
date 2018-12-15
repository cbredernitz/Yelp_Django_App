from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    
    path('buisiness/', views.BusinessListView.as_view(), name='business'),
    path('business/<int:pk>/', views.BusinessDetailListView.as_view(), name='business_detail'),

    path('users/', views.UserListView.as_view(), name='user'),
    path('users/<int:pk>/', views.UserDetailListView.as_view(), name='user_detail'),
    path('user/new/', views.UserCreateView.as_view(), name='user_new'),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),

    path('reivew/', views.ReviewListView.as_view(), name='review'),
    path('review/<int:pk>/', views.ReviewDetailListView.as_view(), name='review_detail'),

    path('search/', views.UserFilterView.as_view(), kwargs=None, name='search'),
]