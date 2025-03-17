from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/')
    age = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(65)], null=True, blank=True)
    STATUS_CHOICES = (
        ('client', 'client'),
        ('owner', 'owner'),
        ('courier', 'courier'),
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='client')
    data_registered = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)


class Store(models.Model):
    store_name = models.CharField(max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='store_list')
    description = models.TextField()
    store_image = models.ImageField(upload_to='store_images/')
    address = models.CharField(max_length=64)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Contact(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='contacts', null=True, blank=True)
    title = models.CharField(max_length=32)
    contact_number = PhoneNumberField()
    social_network = models.URLField(null=True, blank=True)


    def __str__(self):
        return f'{self.title}, {self.contact_number}'


class Product(models.Model):
    product_name = models.CharField(max_length=64)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='client_profile')


class Combo(models.Model):
    combo_name = models.CharField(max_length=64)
    description = models.TextField()
    combo_image = models.ImageField(upload_to='combo_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='combo_list')


    def __str__(self):
        return self.combo_name


class Cart(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products_list')
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)


class Order(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    ORDER_STATUS_CHOICES = (
        ('Ожидает обработки', 'Ожидает обработки'),
        ('Доставлен', 'Доставлен'),
        ('В процессе доставки', 'В процессе доставки'),
        ('Отменен', 'Отменен')
    )
    order_status = models.CharField(max_length=64, choices=ORDER_STATUS_CHOICES, default='Ожидает обработки')
    delivery_address = models.CharField(max_length=128)
    courier = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='courier_profile')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.order_status}'


class Courier(models.Model):
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    current_order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='orders')
    STATUS_CHOICES = (
        ('Доступен', 'Доступен'),
        ('Занят', 'Занят')
    )
    courier_status = models.CharField(max_length=64, choices=STATUS_CHOICES)


    def __str__(self):
        return f'{self.courier}, {self.courier_status}'
class StoreReview(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name='store_review')
    text = models.TextField()
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),
                                                          MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client}, {self.store}'


class CourierRating(models.Model):
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='clients')
    courier = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='couriers')
    rating = models.IntegerField(choices=[(i, str(i))for i in range(1, 6)])
    created_date = models.DateField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f'{self.client}, {self.courier}'






