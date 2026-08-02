from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from cart.models import Cart, CartItem
from .models import Order, OrderItem
# Create your views here.


@login_required
def checkout(request):

    cart = Cart.objects.get(
        user=request.user
    )

    cart_items = CartItem.objects.filter(
        cart=cart
    )

    grand_total = 0

    for item in cart_items:
        grand_total += item.product.price * item.quantity

    order = Order.objects.create(
        user=request.user,
        total_amount=grand_total
    )

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    return redirect('my_orders')





@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-order_date')

    context = {
        'orders': orders
    }

    return render(
        request,
        'my_orders.html',
        context
    )




@login_required
def order_detail(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    order_items = OrderItem.objects.filter(
        order=order
    )

    for item in order_items:
        item.total = item.price * item.quantity

    context = {
        'order': order,
        'order_items': order_items
    }

    return render(
        request,
        'order_detail.html',
        context
    )