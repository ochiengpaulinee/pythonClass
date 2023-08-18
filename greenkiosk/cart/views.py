from django.shortcuts import render,get_object_or_404,redirect
from .models import Cart
from .forms import CartUploadForm

    
def create_cart(request):
    if request.method == 'POST':
        form = CartUploadForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
        return redirect('cart_list')
    else:
        form = CartUploadForm()
        return render(request, 'cart/create_cart.html', {'form': form})
    
def cart_list(request):
    carts = Cart.objects.all()
    return render(request, 'cart/cart_list.html', {'carts': carts})

def cart_detail(request, cart_id):
    cart = get_object_or_404(Cart, pk=cart_id)
    return render(request, 'cart_detail.html', {'cart': cart})




