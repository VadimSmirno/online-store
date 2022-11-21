from django.urls import path
from .views import HistoryOrder,OrderInfo

urlpatterns = [
    path('history/', HistoryOrder.as_view(), name='history'),
    path('order_info/<int:pk>/', OrderInfo.as_view(), name='info')

]