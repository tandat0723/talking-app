from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import Category, Brand, Product, Tag, Banner, Storage, Color, Ram, Comment, User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class StorageSerializer(ModelSerializer):
    class Meta:
        model = Storage
        fields = '__all__'


class ColorSerializer(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class RamSerializer(ModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    image = SerializerMethodField()
    tags = TagSerializer(many=True)
    ram = RamSerializer(many=True)
    color = ColorSerializer(many=True)
    storage = StorageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'ram', 'brand', 'price', 'storage', 'color', 'tags', 'image']

    def get_image(self, obj):
        request = self.context['request']

        if obj.image and not obj.image.name.startswith("/static"):
            path = '/static/%s' % obj.image.name

            return request.build_absolute_uri(path)


class ProductDetailSerializer(ProductSerializer):
    like = SerializerMethodField()
    rating = SerializerMethodField()

    class Meta:
        model = ProductSerializer.Meta.model
        fields = ProductSerializer.Meta.fields + ['description', 'content', 'detail', 'like', 'rating']

    def get_like(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            return obj.like_set.filter(user=request.user, active=True).exists()

    def get_rating(self, obj):
        request = self.context['request']
        if request.user.is_authenticated:
            return obj.rate_set.filter(user=request.user).first()


class BannerSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Banner
        fields = ['id', 'name', 'image']

    def get_image(self, obj):
        request = self.context['request']

        if obj.image and not obj.image.name.startswith('/static'):
            path = '/static/%s' % obj.image.name

            return request.build_absolute_uri(path)


class UserSerializer(ModelSerializer):
    image = SerializerMethodField(source='avatar')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'image', 'password', 'email', 'date_joined']
        extra_kwargs = {
            'password': {
                'write_only': True
            }, 'avatar': {
                'read_only': True,
                'write_only': True
            }
        }

    def get_image(self, obj):
        request = self.context['request']

        if obj.image and not obj.image.name.startswith('/static'):
            path = '/static/%s' % obj.image.name

            return request.build_absolute_uri(path)

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(user.password)
        user.save()

        return user


class CreateCommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'user', 'product']


class CommentSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'created_date', 'updated_date', 'user', 'comment']
