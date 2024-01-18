from django.db import models
from utils.randomic_ import new_slugified

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


    name = models.CharField(max_length = 63)
    slug = models.SlugField(
        unique=True, default=None,
        null=True,blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugified(self.name)
        return super().save(*args, **kwargs)
    

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    title = models.CharField(max_length = 63)
    slug = models.SlugField(
        unique=True, default=None,
        null=True,blank=True, max_length=255
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugified(self.title)
        return super().save(*args, **kwargs)