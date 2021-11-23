from django.urls import path
from web import views


urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('bookings/', views.booking_detail, name='bookings-view'),
]
