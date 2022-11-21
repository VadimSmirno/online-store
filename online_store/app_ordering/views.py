from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Max
from django.shortcuts import redirect
from django.views import generic, View
from app_user.forms import ProfileRedactForm
from .forms import UserInfoForm
from django.shortcuts import render
from app_user.models import Profile
from app_cart.cart import Cart
from .models import Order
from .service import update_order,get_number



class OrderView(generic.TemplateView):

    """"
    Покупка товара незарегистрированным пользователем
    """
    template_name = 'django-frontend/order.html'

    def post(self,request):

        name = self.request.POST['name'].split(' ')
        last_name = name[0].title()
        first_name = name[1].title()
        middle_name = name[2].title()
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            if not User.objects.filter(email=email).exists():
                return redirect('/app_user/login',{'error': 'Пользователь с такой почтой уже зарегистрирован, Вы можете авторизоваться.'})
            else:
                phone = form.cleaned_data.get('telephone_number')
                user = authenticate(request, username=username, password=password)
                login(request, user)
                Profile.objects.create(user_id=request.user.id,middle_name=middle_name, number_phone=phone)
                User.objects.filter(id=self.request.user.id).update(last_name=last_name, first_name=first_name)
                return redirect('/app_ordering/ordering')
        return render(request, 'django-frontend/order.html', {'form':form})


    def get(self, request, *args, **kwargs):
        form = UserInfoForm
        return render(request, 'django-frontend/order.html', {'form':form})



class Ordering(LoginRequiredMixin, generic.FormView):
    template_name = 'django-frontend/order.html'
    form_class = ProfileRedactForm
    login_url = '/app_ordering/ordering_not_authenticated'

    def get_context_data(self, **kwargs):
        context = super(Ordering, self).get_context_data()
        order_info = Order.objects.filter(user_id=self.request.user.id).first()
        context['order_info'] = order_info
        return context

    def get_form_kwargs(self):
        form_kwargs = super(Ordering, self).get_form_kwargs()

        form_kwargs.update({'initial': {
            'last_name': f'{self.request.user.last_name}',
            'first_name': f'{self.request.user.first_name}',
            'email': f'{self.request.user.email}',
            'middle_name': f'{self.request.user.user_info.middle_name}',
            'avatar_img': f'{self.request.user.user_info.avatar_img}',
            'number_phone': f'{self.request.user.user_info.number_phone}'
        }})

        return form_kwargs

    def get_success_url(self):
        return f'/app_ordering/ordering/#step4'

    def form_valid(self, form):
        res = self.request.POST
        cart = Cart(self.request)
        address = res['address']
        city = res['city']
        delivery = res['delivery']
        pay = res['pay']
        number_order = Order.objects.aggregate(Max('number_order'))
        if number_order['number_order__max'] == None:
            number_order['number_order__max'] = 1
        else:
            number_order['number_order__max']+=1
        total_price = cart.get_total_price()
        for item in cart:
            Order.objects.create(
                address=address,
                city=city,
                payment_method=pay,
                delivery_method = delivery,
                user_id=self.request.user.id,
                product = item['product'],
                number_order = number_order['number_order__max'],
                total_price = total_price,
                count_product = item['quantity']
            )
        return super(Ordering, self).form_valid(form)



class PayMethodOnline(View):
    """
    Оплата онлайн картой
    """

    def get(self, request):
        return render(request, 'django-frontend/payment.html')

    def post(self, request):
        user = self.request.user.id
        number = self.request.POST['numero1'].replace(' ','')
        result = get_number(number)
        update_order(result=result,user_id=user)
        cart = Cart(request)
        cart.clear()
        return render(request, 'django-frontend/progressPayment.html', {'result': result} )



class PayMethodRandom(generic.View):
    """
    Оплата со случайного счета
    """

    template_name = 'django-frontend/paymentsomeone.html'

    def get(self, request):
        return render(request, 'django-frontend/paymentsomeone.html')

    def post(self, request):
        user = self.request.user.id

        number = self.request.POST['numero1'].replace(' ','')
        result = get_number(number)
        update_order(result=result,user_id=user)
        cart = Cart(request)
        cart.clear()
        return render(request, 'django-frontend/progressPayment.html', {'result': result} )

