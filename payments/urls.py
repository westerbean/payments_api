from django.urls import path
from .views import PaymentCreateView, PaymentStatusView

urlpatterns = [
    path('payments', PaymentCreateView.as_view(), name='create-payment'),
    path('payments/<int:pk>', PaymentStatusView.as_view(), name='payment-status'),
]
