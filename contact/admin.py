from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    '''
    display contact fields
    '''
    list_display = (
        'first_name',
        'last_name',
        'email',
    )

    readonly_fields = (
        'message',
        'date',
    )


# register models
admin.site.register(Contact, ContactAdmin)
