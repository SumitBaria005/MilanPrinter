from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import field_mapping
from .models import Category


class CategorySerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
