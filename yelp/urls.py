from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    # path('buisiness/', views.BusinessListView.as_view(), name='business'),
    # path('business/<int:pk>/', views.BusinessReviewView.as_view(), name='review'),
]