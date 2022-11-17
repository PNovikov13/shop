from django.conf import settings
from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price' : str(product.price)
                                     }
        if update_count:
            self.cart[product_id]['quantity'] = count
        else:
            self.cart[product_id]['quantity'] += count

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def delete(self, product):

        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        id = self.cart.keys()
        products = Product.objects.filter(id__in= id)
        for product in products:
            self.cart[str(product.id)]['product'] = product
        for elem in self.cart.values():

            elem['total_price'] = elem['quantity'] * float(elem['price'])
            yield elem

    def __len__(self):
        summ = 0
        for elem in self.cart.values():
            summ += elem['quantity']
        return summ

    def get_total_price(self):
        full_sum = 0
        for elem in self.cart.values():
            full_sum += elem['quantity'] * float(elem['price'])
        return full_sum

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
