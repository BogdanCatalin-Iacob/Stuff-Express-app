from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    '''

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        # query for specific category by navbar menu
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        # query on search box
        if 'query' in request.GET:
            search_query = request.GET['query']
            if not search_query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            # search based on name or description
            queries = Q(name__icontains=search_query) | Q(
                description__icontains=search_query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'curent_categories': categories,
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
