from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from .models import Profile
from .forms import UserRegistrationForm, ProfileRedactForm
from app_ordering.models import Order


def register(request):
    """регистрация пользователя"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            password1 = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)
            login(request, user)
            Profile.objects.create(user_id=request.user.id)
            return redirect('/app_product/home')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'django-frontend/registrations.html', {'user_form': user_form})



class UserDetaileViewPersonalArea(generic.DetailView):
    """информация личного кабинета"""
    model = User
    template_name = 'django-frontend/account.html'
    context_object_name = 'user_detail'

    def get_context_data(self, **kwargs):
        context = super(UserDetaileViewPersonalArea, self).get_context_data(**kwargs)
        history_order = Order.objects.filter(user_id=self.request.user.id)[:5]
        context['history_order'] = history_order
        return context



class AuthenticationLogoutView(LogoutView):
    """Выйти из учетной записи"""
    template_name = 'django-frontend/catalog.html'

    def get_success_url(self):
        return '/app_product/home'



class AuthenticationLoginView(LoginView):
    """Аутентификация"""
    template_name = 'django-frontend/login.html'



class RedactProfileView(FormView):
    template_name = 'django-frontend/profile.html'
    form_class = ProfileRedactForm

    def get_success_url(self):
        pk = self.request.user.id
        success_url = f'/app_user/personal_area/{pk}'
        return success_url

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        avatar_img = form.cleaned_data.get('photo_avatar')
        password1 = form.cleaned_data.get('password1')
        number_phone = form.cleaned_data.get('number_phone')
        email = form.cleaned_data.get('email')
        last_name = name[0].title()
        first_name = name[1].title()
        middle_name = name[2].title()
        Profile.objects.filter(id=self.request.user.user_info.id). \
            update(middle_name=middle_name, avatar_img=avatar_img, number_phone=number_phone)
        User.objects.filter(id=self.request.user.id). \
            update(first_name=first_name, last_name=last_name, email=email)
        user = User.objects.get(id=self.request.user.id)
        if password1 != '':
            user.set_password(password1)
            user.save()
        user = authenticate(username=self.request.user, password=password1)
        login(self.request, user)
        return super().form_valid(form)

    def get_form_kwargs(self):
        form_kwargs = super(RedactProfileView, self).get_form_kwargs()

        form_kwargs.update({'initial': {
            'last_name': f'{self.request.user.last_name}',
            'first_name': f'{self.request.user.first_name}',
            'email': f'{self.request.user.email}',
            'middle_name': f'{self.request.user.user_info.middle_name}',
            'avatar_img': f'{self.request.user.user_info.avatar_img}',
            'number_phone': f'{self.request.user.user_info.number_phone}'
        }})

        return form_kwargs
