from django.shortcuts import render

# Create your views here.
# core/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PaymentDetails
from .serializers import PaymentDetailsSerializer

@api_view(['GET'])
def get_payment_details(request):
    obj = PaymentDetails.objects.first()
    serializer = PaymentDetailsSerializer(obj)
    return Response(serializer.data)
