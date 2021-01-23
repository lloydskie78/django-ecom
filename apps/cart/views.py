from django.shortcuts import render, redirect
from django.conf import settings

from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    productsString = ""

    for item in cart:
        product = item["product"]
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (
            product.id,
            product.title,
            product.price,
            item["quantity"],
            item['total_price']
        )

        productsString = productsString + b

    context = {
        "cart": cart, 
        "pub_key": settings.STRIPE_API_KEY_PUBLISHABLE, 
        "productsString": productsString.rstrip(",")
        }

    return render(request, "cart.html", context)

def success(request):
    return render(request, "success.html")
