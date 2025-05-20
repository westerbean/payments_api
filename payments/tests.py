from django.test import TestCase
from rest_framework.test import APIClient

class PaymentAPITest(TestCase):
    def test_payment(self):
        client = APIClient()
        data = {
            "name": "Jane Doe",
            "email": "jane@example.com",
            "amount": "1000",
            "gateway": "paystack"
        }
        response = client.post("/api/v1/payment/", data, format='json')
        self.assertEqual(response.status_code, 200)
