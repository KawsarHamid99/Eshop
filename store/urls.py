from django.urls import path
from . import views
from .views import loginForm,Signup,Index,Logout,cart_view,Checkout,OrderView,not_String
urlpatterns=[
    
    path("",Index),
    path("signup/",Signup,name="signup"),
    path("login/",loginForm,name="login"),
    path("logout/",Logout,name="logout"),
    path("cart/",cart_view,name="cart"),
    path("check-out/",Checkout.as_view(),name="checkout"),
    path("order/",OrderView.as_view(),name="order"),
]