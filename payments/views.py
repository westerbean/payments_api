from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentCreateSerializer, PaymentStatusSerializer
from .utils import simulate_payment_gateway

class PaymentCreateView(APIView):
    def post(self, request):
        serializer = PaymentCreateSerializer(data=request.data)
        if serializer.is_valid():
            payment = serializer.save()
            result = simulate_payment_gateway(payment)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PaymentStatusView(APIView):
    def get(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
            serializer = PaymentStatusSerializer(payment)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)
