from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import ContactForm


def contact(request):
    '''
    Contact form to send an email to admin
    '''
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you! \
                Your message was successfully sent.\
                We'll get in touch soon!")
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Your message was not sent!\
                Please, try again.')
            return redirect(reverse('contact'))

    form = ContactForm()

    template = 'contact/contact_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
