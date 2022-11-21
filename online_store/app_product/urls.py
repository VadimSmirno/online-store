from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.HomeView.as_view(), name='home'),
    path('catalog/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),
    path('product_detail/<int:pk>', views.ProductDetail.as_view(), name='product_detail'),
    path('subcatalog/<int:pk>', views.SubCtegoryDetail.as_view(), name='subcategory_detail'),

]
