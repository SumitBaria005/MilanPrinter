from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.HyperlinkedModelSerializer):

    written_image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=False, required=True)

    class Meta:
        model = Order
        fields = ['user', 'product_name', 'no_of_copies',
                  'transaction_id', 'total_amount', 'written_image']
        # add product and quentity
        # ['user', 'product_name', 'no_of_copies'
        # 'transaction_id', 'total_amount', 'written_image']
