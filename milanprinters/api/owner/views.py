
from .serializers import OwnerSerializer
from rest_framework import viewsets
from .models import Owner

# Create your views here.


class OwnerViewset(viewsets.ModelViewSet):
    queryset = Owner.objects.all().order_by('name')
    serializer_class = OwnerSerializer
