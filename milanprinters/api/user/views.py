from rest_framework import decorators, viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt


import random
import re

# Create your views here.


def generate_session_token(length=10):
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)]) for _ in range(length))


@csrf_exempt
def sigin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Send Post request with valid parameters'})

    username = request.POST['email']
    password = request.POST['password']

    # validation Process
    if not re.match("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", username):
        return JsonResponse({'error': 'Please Enter valid email address!'})

    if len(password) < 3:
        return JsonResponse({'error': 'Please Enter Password Greater then 3 letters!'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)

        if user.check_password(password):
            usr_dict = UserModel.objects.filter(
                email=username).values().first()
            usr_dict.pop('password')

            if user.session_token != '0':
                user.session_token = '0'
                user.save()
                return JsonResponse({'error': 'Previous Session already exists!'})

            token = generate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})

        else:
            return JsonResponse({'error': 'Please Enter Valid Password!'})

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Please Enter Valid Username Or Passwrod !'})


def signout(request, id):
    logout(request)

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        user.session_token = '0'
        user.save()

    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Enter Valid UserID'})

    return JsonResponse({'success': 'Successfully Logout'})


class UserViewset(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
