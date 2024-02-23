
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('notifications/', views.notifications, name="notifications"),
    path('account/login/', views.login, name="account"),
    path('cart/', views.cart, name="cart"),
    path('products/<int:myid>', views.productView, name="products"),
    path('cart/placeOrder/', views.placeOrder, name='placeOrder'),
    path('search/', views.search, name='Search'),
    path('account/signup/', views.signup, name='Signup'),
    path('account/forgot/', views.forgot, name='Forgot'),
    path('account/', views.account, name='Account'),
]