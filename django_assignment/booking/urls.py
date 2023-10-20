# accounts/urls.py

from django.urls import path
from .views import register_user, user_login, user_logout, ResourceList, UserBookings, CreateBooking

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('resources/', ResourceList.as_view(), name='resource-list'),
    # path('book-resource/', BookResource.as_view(), name='book-resource'),
    path('bookings/', UserBookings.as_view(), name='user-bookings'),
    path('bookings/create/', CreateBooking.as_view(), name='create-booking'),
]