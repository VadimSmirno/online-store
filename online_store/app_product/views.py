from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import FormView
from app_cart.forms import CartAddProductForm
from .models import Product, Category, Subcategory, Reviews
from random import randint
from .forms import FilterForms, SortedForms, ReviewForms
from django.db.models import Count


class HomeView(generic.View):
    """
    Отбражение главной страницы
    """

    def get(self,request):
        """

        рандомные категории на главной странице
        """
        product_pieces_left = Product.objects.order_by('-pieces_left')[:5].select_related('product_category')
        product_number_of_sales = Product.objects.order_by('number_of_sales')[:8].select_related('product_category')
        number_1 = randint(14,24)
        random_product = Product.objects.filter(product_category_id__id__gte=number_1,
                                     product_category_id__id__lte=number_1+3)[:3].select_related('product_category')
        return render(request, 'django-frontend/index.html', {
                                                                'product_pieces_left':product_pieces_left,
                                                                'product_number_of_sales':product_number_of_sales,
                                                                'random_product' : random_product,
                                                              }
                      )


class CategoryDetail(generic.DetailView):

    """ Отображение категорий """

    model = Category
    template_name = 'django-frontend/catalog.html'
    context_object_name = 'category_detail'


    def get_context_data(self, **kwargs):
        context = super(CategoryDetail,self).get_context_data()
        form = FilterForms()
        form_sorted = SortedForms()
        context['form_sorted'] = form_sorted
        context['form'] = form
        sorted = self.request.GET.get('value')
        pk=self.kwargs['pk']
        if sorted != None:
            sorted_product=Product.objects.filter(product_category_id=pk).order_by(f'-{sorted}')
            context['sorted_product'] = sorted_product
            return context
        return context

    def post(self,request, pk):
        form = FilterForms(request.POST)
        if form.is_valid() :
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            products_in_stock = form.cleaned_data.get('products_in_stock')
            free_shipping = form.cleaned_data.get('free_shipping')
            price = price.split(';')
            filter_product = Product.objects.filter(price__gte=int(price[0]),
                                                    price__lte=int(price[1]),
                                                    product_category_id=pk,
                                                    name__icontains=name,
                                                    free_delivery=free_shipping,
                                                    products_in_stock=products_in_stock
                                                    )

            return render(request, 'django-frontend/catalog.html', {'filter_product': filter_product, 'form': form, 'pk': pk})
        else:
            return redirect(f'/app_product/catalog/{pk}')

class SubCtegoryDetail(generic.DetailView):

    """Отображение подкатегорий"""
    model = Subcategory
    template_name = 'django-frontend/subcatalog.html'
    context_object_name = 'subcategory_detail'

    def get_context_data(self, **kwargs):
        context = super(SubCtegoryDetail,self).get_context_data()
        form = FilterForms()
        form_sorted = SortedForms()
        context['form_sorted'] = form_sorted
        context['form'] = form
        return context

    def post(self,request, pk):
        form = FilterForms(request.POST)
        form_sorted = SortedForms(request.POST)
        if form_sorted.is_valid():
            price_sorted = form_sorted.cleaned_data.get('price')
            print(price_sorted)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            price = form.cleaned_data.get('price')
            products_in_stock = form.cleaned_data.get('products_in_stock')
            free_shipping = form.cleaned_data.get('free_shipping')
            price = price.split(';')
            filter_product = Product.objects.filter(price__gte=int(price[0]),
                                                    price__lte=int(price[1]),
                                                    subcategory_id=pk,
                                                    name__icontains=name,
                                                    free_delivery=free_shipping,
                                                    products_in_stock=products_in_stock
                                                    )
            return render(request, 'django-frontend/subcatalog.html', {'filter_product': filter_product, 'form': form})
        else:
            return redirect(f'/app_product/subcatalog/{pk}')


class ProductDetail(generic.DetailView, FormView):

    """Информация о продукте"""

    template_name = 'django-frontend/product.html'
    context_object_name = 'product_detail'
    form_class = ReviewForms

    def get_queryset(self):
        return Product.objects.all().prefetch_related('product_review').select_related('product_category')

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        form_add_cart = CartAddProductForm()
        context['form_add_cart'] = form_add_cart
        result = Reviews.objects.filter(review_product__id=self.kwargs['pk']).select_related('author')
        count_review = Product.objects.filter(id = self.kwargs['pk']).annotate(product_reviews=Count('product_review__id'))
        count_review = count_review[0].product_reviews
        context['count_review'] = count_review
        context['result'] = result
        return context

    def get_success_url(self):
        pk = self.kwargs['pk']
        return f'/app_product/product_detail/{pk}'


    def form_valid(self, form):
        instans = Product.objects.filter(id=self.kwargs['pk'])
        body = form.cleaned_data.get('body')
        res = Reviews.objects.create(descriptions = body, author_id=self.request.user.id)
        res.review_product.set(instans)
        return super().form_valid(form)

