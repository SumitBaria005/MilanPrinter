

from django.urls import path, include
from .views import home


urlpatterns = [
    path('', home, name="api"),
    path('category/', include('api.category.urls')),
    path('product/', include('api.product.urls')),
    path('owner/', include('api.owner.urls')),
    path('user/', include('api.user.urls')),
    path('order/', include('api.order.urls')),
    path('payment/', include('api.payment.urls'))
]
