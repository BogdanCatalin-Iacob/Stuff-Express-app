from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .forms import ContactForm


def contact(request):
    '''
    Contact form to send an email to admin
    '''
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email_data = form.save(commit=False)
            # get email subject txt
            email_subject = render_to_string(
                'contact/confirmation_emails/confirmation_email_subject.txt',
                {'email_data': email_data})
            # get email body txt
            email_body = render_to_string(
                'contact/confirmation_emails/confirmation_email_body.txt',
                {'email_data': email_data,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            user_email = email_data.email
            email_data.save()

            messages.success(request, "Thank you! \
                Your message was successfully sent.\
                We'll get in touch soon!")
            return redirect(reverse('products'))
        else:
            messages.error(request, 'Your message was not sent!\
                Please, try again.')
            return redirect(reverse('contact'))

        # send email
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [user_email])

    form = ContactForm()

    template = 'contact/contact_form.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
