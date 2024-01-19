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
    
    def __str__(self) -> str:
        return self.name
    

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

    def __str__(self) -> str:
        return self.title 
    
class Page(models.Model):
    
    title = models.CharField(max_length=50)
    slug = models.SlugField(
        unique=True,default=None,
        null=False,blank=True,max_length=255
    )
    is_published = models.BooleanField(
        default=False,
        help_text = '"Está publicado", se o campo estiver marcado, esta página será exibida'
        )
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugified(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    title = models.CharField(max_length=65,)
    slug = models.SlugField(
        unique=True,default=None,
        null=False,blank=True,max_length=255
    )
    excerpt = models.CharField(max_length=150)
    is_published = models.BooleanField(
        default=False,
        help_text = '"Está publicado", se o campo estiver marcado, este post será exibida'
        )
    content = models.TextField()
    cover = models.ImageField(upload_to='posts/%Y/%m',blank=True,default='')
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text = 'Exibir imagem de capa no conteúdo do post?'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True,default=None)
    tag = models.ManyToManyField(Tag,blank=True,default='')

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = new_slugified(self.title)
        return super().save(*args, **kwargs)    