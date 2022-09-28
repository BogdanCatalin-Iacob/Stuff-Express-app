from django.shortcuts import render, redirect, reverse, HttpResponse


def view_bag(request):
    '''
    A view to display bag content
    '''
    return render(request, 'bag/bag.html')


# from code institute
def add_to_bag(request, item_id):
    '''
    Add to bag products of specified quantity
    '''

    # get the quantity selected by user
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # set the user selected size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # check if bag exist in session else create an empty dict
    bag = request.session.get('bag', {})

    # add items to the bag with multiple sizes
    if size:
        # if the item already exist with the same size increase quantity
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # set the item quantity if item has no sizes
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    # set the bag items into session
    request.session['bag'] = bag

    return redirect(redirect_url)


# from code institute
def adjust_bag(request, item_id):
    '''
    Adjust the quantity of selected product
    '''

    # get the quantity selected by user
    quantity = int(request.POST.get('quantity'))

    # set the user selected size
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    # check if bag exist in session else create an empty dict
    bag = request.session.get('bag', {})

    # update item quantity
    if size:
        # if the item already exist with the same size increase quantity
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    else:
        # update item quantity if item has no sizes
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    # set the bag items into session
    request.session['bag'] = bag

    return redirect(reverse('view_bag'))


# from code institute
def remove_from_bag(request, item_id):
    '''
    Remove the item from bag
    '''

    try:
        # set the user selected size
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']

        # check if bag exist in session else create an empty dict
        bag = request.session.get('bag', {})

        # delete item by size
        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            # delete item if has no sizes
            bag.pop(item_id)

        # set the bag items into session
        request.session['bag'] = bag

        return HttpResponse(status=200)
    except Exception:
        return HttpResponse(status=500)
