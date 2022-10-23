from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from profiles.models import UserProfile


class Category(models.Model):

    class Meta:
        '''
        Fix the plural of categories name in django admin panel
        '''
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    created_by = models.CharField(
        max_length=254, null=True, blank=True, editable=False)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    brand = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    size_xs = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=False, blank=False, default=0)
    size_s = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=False, blank=False, default=0)
    size_m = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=False, blank=False, default=0)
    size_l = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=False, blank=False, default=0)
    size_xl = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(999)],
        null=False, blank=False, default=0)

    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    market_price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user_review')
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='product_review')
    date = models.DateTimeField(auto_now_add=True)
    review_text = models.TextField(null=True, blank=True)
    star_rating = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return str(self.pk)
