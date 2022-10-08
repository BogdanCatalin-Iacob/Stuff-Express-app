from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=3000, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name
