from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    '''

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'query' in request.GET:
            search_query = request.GET['query']
            if not search_query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # search based on name or description
            queries = Q(name__icontains=search_query) | Q(
                description__icontains=search_query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    '''
    A view to show individual product details
    '''

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
