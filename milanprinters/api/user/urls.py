
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.UserViewset)


urlpatterns = [

    path('login/', views.sigin, name='signin'),
    path('logout/<int:id>', views.signout, name='signout'),
    path('', include(router.urls)),
]
