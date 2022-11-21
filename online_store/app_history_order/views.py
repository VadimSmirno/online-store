from django.views import generic
from app_ordering.models import Order



class HistoryOrder(generic.ListView):
    """"
    История покупок
    """""
    model = Order
    template_name = 'django-frontend/historyorder.html'
    context_object_name = 'history'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)



class OrderInfo(generic.ListView):
    """""
    Информация о заказах
    """""
    model = Order
    template_name = 'django-frontend/oneorder.html'
    context_object_name = 'order_info'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderInfo, self).get_context_data()
        order = Order.objects.filter(user_id=self.request.user.id, number_order=self.kwargs['pk']). \
            select_related('product'). \
            select_related('user')
        context['order'] = order
        return context

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id, number_order=self.kwargs['pk']). \
                   select_related('product'). \
                   select_related('user')[:1]
