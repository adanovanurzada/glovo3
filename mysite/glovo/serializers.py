from .models import *
from rest_framework import serializers

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'status']

class UserProfileClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class CategoryListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']

class CategorySimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'product_image', 'description', 'price']

class ProductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'product_image', 'description', 'price', 'store']


class ComboListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['combo_name', 'combo_image', 'description', 'price']

class ComboDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Combo
        fields = ['id', 'combo_name', 'combo_image', 'description', 'price', 'store']


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['title', 'contact_number', 'social_network']


class CartSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'


class CourierSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'



class StoreReviewSimpleSerializers(serializers.ModelSerializer):
    client = UserProfileClientSerializers()
    created_date = serializers.DateTimeField(format('%d-%m-%Y %H:%M'))
    class Meta:
        model = StoreReview
        fields = ['client', 'text', 'stars', 'created_date']

class StoreReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = StoreReview
        fields = '__all__'

class CourierRatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = CourierRating
        fields = '__all__'

class StoreListSerializers(serializers.ModelSerializer):
    category = CategorySimpleSerializers()
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'store_image', 'category']

class StoreDetailSerializers(serializers.ModelSerializer):
    category = CategorySimpleSerializers()
    owner = UserProfileSimpleSerializers()
    contacts = ContactSerializers(many=True, read_only=True)
    products_list = ProductListSerializers(many=True, read_only=True)
    combo_list = ComboListSerializers(many=True, read_only=True)
    store_review = StoreReviewSimpleSerializers(many=True, read_only=True)
    class Meta:
        model = Store
        fields = ['store_name', 'store_image', 'category', 'description', 'address', 'contacts',
                  'owner', 'products_list', 'combo_list', 'store_review']


class CategoryDetailSerializers(serializers.ModelSerializer):
    store_list = StoreListSerializers(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'store_list']


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'




