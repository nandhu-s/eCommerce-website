from django.contrib import admin
from django.urls import path
from .views import *
from .middleware.authentication import authentication


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('website', website , name='website'),
    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', authentication(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', authentication(Orders.as_view()), name='orders'),
]