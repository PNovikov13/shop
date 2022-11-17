from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import AddForm


#  get_object_or_404 - SELECT WHERE
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(avaliable=True)
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    print(categories)
    print(products)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'products': products, 'categories': categories})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id, avaliable=True)
    cart_product_form = AddForm()
    return render(request, 'shop/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})
