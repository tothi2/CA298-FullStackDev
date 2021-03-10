from django.urls import path
from . import views
from .forms import UserLoginForm

urlpatterns = [
 path('', views.index, name="index"),
 path('registration/', views.register, name="register"),  # /registration
 path('allproducts/', views.all_products, name="all_products"),
 path('singleproduct/<int:prodid>', views.singleproduct, name="product_single"),
 path('myform/', views.myform),
 path('usersignup/', views.CaUserSignupView.as_view(), name="register"),
 path('adminsignup/', views.AdminSignupView.as_view(), name="Admin register"),
 path('login/', views.Login.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
 path('logout/', views.logout_view, name="logout")
]
