from rest_framework import serializers
from .models import PaymentDetails

class PaymentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['card1_name', 'card1_account', 'card2_name', 'card2_account']
