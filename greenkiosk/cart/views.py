from django.shortcuts import render,redirect
from .models import Cart
from inventory.models import Product
# from .forms import CartUploadForm
# Create your views here.

# def add_to_cart(request, product_id):
#     product = Product.objects.get(id=product_id)
#     user = request.user
#     cart = Cart.objects.filter(user=user).first()
#     if not cart:
#         cart = Cart.objects.create(user=user)
#     cart.products.add(product)
#     return redirect('view_cart')

def view_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user).prefetch_related('products')
    total_price = sum(product.price * product.quantity for cart in cart_items for product in cart.products.all())
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/view_cart.html', context)