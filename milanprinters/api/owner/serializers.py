
from rest_framework import serializers
from .models import Owner


class OwnerSerializer(serializers.HyperlinkedModelSerializer):

    image = serializers.ImageField(
        max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Owner
        fields = ['name', 'description', 'image']
