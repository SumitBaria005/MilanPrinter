
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializers

# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializers
