from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(blank=True, upload_to="users/%Y/%m")


class Banner(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to='banners/%Y/%m')


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100, blank=False, unique=True)

    def __str__(self):
        return self.name


class Brand(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('category', 'name')
        ordering = ['name']


class Product(BaseModel):
    name = models.CharField(max_length=100, blank=False, unique=True)
    image = models.ImageField(blank=True, upload_to='products/%Y/%m')
    price = models.CharField(max_length=13)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    storage = models.ManyToManyField("Storage", related_name='storages')
    color = models.ManyToManyField("Color", related_name='colors')
    ram = models.ManyToManyField("Ram", related_name='rams')
    tags = models.ManyToManyField('Tag', related_name='products', blank=True)
    description = RichTextField()
    content = RichTextField()
    detail = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'brand')
        ordering = ['name']


class Storage(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Ram(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Color(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Comment(BaseModel):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.user


class Tag(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class ProductView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_date = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.views

    class Meta:
        unique_together = ('user', 'product')


class Delivery(BaseModel):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ActionBase(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'product')
        abstract = True


class Rate(ActionBase):
    rate = models.SmallIntegerField(default=0)


class Like(ActionBase):
    active = models.BooleanField(default=False)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.CharField(max_length=20)
    count = models.IntegerField(default=0)


class OrderDetail(BaseModel):
    order = models.ForeignKey(Order, related_name='order_detail', on_delete=models.CASCADE)
    quantity = models.CharField(max_length=2)
    total = models.CharField(max_length=14)

    def __str__(self):
        return self.order
