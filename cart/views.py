from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product
# Create your views here.

@login_required
def add_to_cart(request, product_id):
    product=get_object_or_404(Product,id=product_id)

    cart, created=Cart.objects.get_or_create(user=request.user)

    cart_item, created=CartItem.objects.get_or_create(cart=cart,product=product,defaults={'quantity':1})

    if not created:
        cart_item.quantity+=1
        cart_item.save()

    return redirect('home')


@login_required
def cart(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    grand_total = 0

    for item in cart_items:

        item.total = item.product.price * item.quantity

        grand_total += item.total

    context = {
        'cart_items': cart_items,
        'grand_total': grand_total
    }

    return render(request,'cart.html',context)


@login_required
def increase_quantity(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart_item.quantity += 1

    cart_item.save()

    return redirect('cart')


@login_required
def decrease_quantity(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if cart_item.quantity > 1:

        cart_item.quantity -= 1

        cart_item.save()

    else:

        cart_item.delete()

    return redirect('cart')



@login_required
def remove_item(request, item_id):

    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart_item.delete()

    return redirect('cart')