from django.urls import path
from .views import Ordering, OrderView, PayMethodOnline, PayMethodRandom

urlpatterns = [
    path('ordering/',Ordering.as_view()),
    path('ordering_not_authenticated/', OrderView.as_view()),
    path('pay_method_online/', PayMethodOnline.as_view(), name = 'online'),
    path('pay_method_random/', PayMethodRandom.as_view(), name = 'random'),
]