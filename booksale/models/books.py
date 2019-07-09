from django.db import models
from django.contrib.auth.models import User
from .users import Profile
from django.core.validators import  MinValueValidator

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Mystery', 'Mystery'),
        ('Biographies', 'Biographies'),
        ('Sci-fi', 'Sci-fi and Fantasy'),
        ('Horror', 'Horror'),
        ('Kids', 'Kids'),
        ('Comics', 'Comics'),
        ('generic','generic')
    ]
    categ = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='generic')


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    published = models.DateTimeField()
    price = models.DecimalField(max_digits=4, decimal_places=2)
    stock = models.IntegerField(validators=[
            MinValueValidator(1)
        ])
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    class Meta:
        ordering = ('title',)


