from django.shortcuts import (
    render, get_object_or_404, redirect, reverse, HttpResponse)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile


# based on code institute django module
def all_products(request):
    '''
    A view to show all products, including sorting and search queries
    '''
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # query by sorting products
        if 'sort' in request.GET:
            sort_key = request.GET['sort']
            sort = sort_key
            # case insensitive sorting
            if sort_key == 'name':
                sort_key = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if sort_key == 'category':
                sort_key == 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                # reverse sorting direction
                if direction == 'desc':
                    sort_key = f'-{sort_key}'
            products = products.order_by(sort_key)

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

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }
    return render(request, 'products/products.html', context)


# from code institute
def product_detail(request, product_id):
    '''
    A view to show individual product details
    '''
    user = request.user
    product = get_object_or_404(Product, pk=product_id)

    # get review if exists
    reviews = Review.objects.filter(product=product_id)

    context = {
        'product': product,
        'reviews': reviews,
        'user': user,
    }
    return render(request, 'products/product_detail.html', context)


# from code institute
@login_required
def add_product(request):
    """ Add a product to the store """
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.created_by = user
            product.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    '''
    Edit an existing product
    '''
    product = get_object_or_404(Product, pk=product_id)
    # check if the user is superuser or owner
    if not request.user.is_superuser:
        if request.user != product.created_by.user:
            messages.error(request, 'Sorry, section for products owners only')
            return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    '''
    Delete a product from db
    '''
    product = get_object_or_404(Product, pk=product_id)
    if not request.user.is_superuser:
        if request.user != product.created_by.user:
            messages.error(request, 'Sorry, section for products owners only')
            return redirect(reverse('home'))

    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


def review(request, product_id):
    '''
    Product star review with or without text review
    '''
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user
            review.product = product
            review.save()
            messages.success(request, 'Your review was successfully posted!')
        else:
            messages.error(request, 'Review posting failed!')

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def edit_review(request, product_id, review_id):
    '''
    Edit an existing review
    '''
    if request.user.is_authenticated:
        product = get_object_or_404(Product, pk=product_id)
        review = get_object_or_404(Review, pk=review_id)

    # check if logged user is the same as the initial writter
    if request.user.id == review.user.id:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                messages.success(request, 'Successfully updated review!')
            else:
                messages.error(request, 'Failed to update review.')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            form = ReviewForm(instance=review)

        template = 'products/edit_review.html'
        context = {
            'form': form,
            'product': product,
            'review': review,
            }
        return render(request, template, context)

    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def delete_review(request, review_id):
    '''
    Delete a product from db
    '''
    try:
        review = get_object_or_404(Review, pk=review_id)
        product = get_object_or_404(Product, pk=review.product.id)
        review.delete()
        messages.success(request, 'Review successfully deleted!')
        return redirect(reverse('product_detail', args=[product.id]))
    except Exception:
        messages.error(request, 'Could not delete your review')
        return HttpResponse(status=500)
