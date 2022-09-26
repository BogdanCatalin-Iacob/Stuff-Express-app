from django.shortcuts import render, redirect


def view_bag(request):
    '''
    A view to display bag content
    '''
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    '''
    Add to bag products of specified quantity
    '''

    # get the quantity selected by user
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    # check if bag exist in session else create an empty dict
    bag = request.session.get('bag', {})

    # set the item quantity
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    # set the bag items into session
    request.session['bag'] = bag
    print(request.session['bag'])

    return redirect(redirect_url)
