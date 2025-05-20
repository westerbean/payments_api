from rest_framework import serializers
from .models import Payment

class PaymentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'name', 'email', 'amount', 'gateway']

class PaymentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'name', 'email', 'amount', 'gateway', 'status', 'reference', 'created_at', 'message']
