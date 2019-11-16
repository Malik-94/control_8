from django.urls import path
from webapp.views.product import IndexView, ProductView, ProductCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product/<int:pk>/', ProductView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
]

app_name = 'webapp'