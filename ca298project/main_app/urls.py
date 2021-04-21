from django.urls import path, include
from . import views
from .forms import UserLoginForm
from rest_framework import routers, serializers, viewsets
from .models import CaUser, Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CaUser
        fields = ['url', 'user_name', 'email', 'is_staff']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class UserViewSet(viewsets.ModelViewSet):
    queryset = CaUser.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.register, name="register"),  # /registration
    path('allproducts/', views.all_products, name="all_products"),
    path('singleproduct/<int:prodid>', views.singleproduct, name="product_single"),
    path('myform/', views.myform),
    path('usersignup/', views.CaUserSignupView.as_view(), name="register"),
    path('adminsignup/', views.AdminSignupView.as_view(), name="Admin register"),
    path('login/', views.Login.as_view(template_name="login.html", authentication_form=UserLoginForm), name='login'),
    path('logout/', views.logout_view, name="logout"),
    path('addbasket/<int:prodid>',views.add_to_basket, name="add_to_basket"),
    path('basket/', views.get_basket, name="basket"),
    path('basketremove/<int:sbi>', views.remove_from_basket, name="remove_basket"),
    path('checkout/', views.order_form, name="checkout"),
    path('api/', include(router.urls))
]
