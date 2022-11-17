from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .cart import Cart
from shop.models import Product
from .forms import AddForm


# Create your views here.

@require_POST
def add_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = AddForm(request.POST)
    if form.is_valid():
        tmp = form.cleaned_data
        cart.add(product, tmp['quantity'], tmp['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.delete(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/detail.html', context=context)
