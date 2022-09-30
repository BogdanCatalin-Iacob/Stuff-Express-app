from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe


def checkout(request):
    '''
    Check if bag has items and
    create a new OrderForm instance
    '''
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    # get the grand total from bag_contents
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LRSjYGg4BpUsp5D5kJqxadDjW64t7xzSQshpH9UBEbzHHYK71gHmt2L6A6QNwrCWS3LMiZHEqdguKNnj8fV681P00dxo6Pztx',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
