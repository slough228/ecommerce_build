import random
import os
from django.db import models
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator


def get_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    '''Protect from bad names'''
    # print(instance)
    # print(filename)
    new_filename = random.randint(1, 90384712023)
    name, ext = get_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename,
                                                             final_filename=final_filename)


class ProductManager(models.Manager):
    def featured(self):
        return self.get_queryset().filter(featured=True)

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.99)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=False)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}".format(slug=self.slug)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_receiver, sender=Product)
