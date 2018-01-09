from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework import serializers
from .models import Login, Products, WishList

class LoginSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'


class ProductSerialzer(serializers.ModelSerializer):
    pImage = serializers.SerializerMethodField('get_image')
    def get_image(self, obj):
        return obj.pImage.url

    class Meta:
        model = Products
        fields = '__all__'

class WishListSerialzer(serializers.ModelSerializer):
    product = PresentablePrimaryKeyRelatedField(
		queryset=Products.objects,
		presentation_serializer=ProductSerialzer
	)
    class Meta:
        model = WishList
        fields = '__all__'