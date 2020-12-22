
from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

from .models import Order
from .serializers import OrderSerializer

# Create your views here.


def validate_user_token(id, token):
    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False

    except UserModel.DoesNotExist:
        return False


@csrf_exempt
def add(request, id, token):
    if not validate_user_token(id, token):
        return JsonResponse({'error': 'Please Login First'})

    if request.method == 'POST':
        user_id = id
        product = request.POST['product']
        transaction_id = request.POST['transaction_id']
        amount = request.POST['amount']
        image = request.POST['image']
        quantity = request.POST['quantity']
        total_amount = amount*quantity

        UserModel = get_user_model()

        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return JsonResponse({'error': 'Please enter valide UserID'})

        ordr = Order(user=user, product_name=product, no_of_copies=quantity,
                     transaction_id=transaction_id, total_amount=total_amount, written_image=image)
        ordr.save()
        return JsonResponse({'success': True, 'error': False, 'msg': 'Order Placed Successfully'})


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
