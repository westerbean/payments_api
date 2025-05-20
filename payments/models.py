from django.db import models

class Payment(models.Model):
    GATEWAY_CHOICES = [
        ('paystack', 'Paystack'),
        ('flutterwave', 'Flutterwave'),
        ('paypal', 'PayPal'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    gateway = models.CharField(max_length=20, choices=GATEWAY_CHOICES)
    status = models.CharField(max_length=20, default='pending')
    reference = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.name} - {self.gateway} - {self.status}"
