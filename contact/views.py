from django.shortcuts import render, reverse, HttpResponse
from .forms import ContactForm


def contact(request):

    form = ContactForm()

    template = 'contact/contact_form.html'
    context = {
        'form': form,
    }

    return render(request, template)
