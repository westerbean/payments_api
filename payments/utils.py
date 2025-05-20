import uuid

def simulate_payment_gateway(payment):
    fake_reference = str(uuid.uuid4())
    payment.reference = fake_reference
    payment.status = 'completed'
    payment.message = 'Payment details retrieved successfully'
    payment.save()

    return {
        "id": payment.id,
        "status": "initiated",
        "reference": fake_reference,
        "redirect_url": f"https://{payment.gateway}.com/checkout/{fake_reference}",
        "message": "Payment initiated"
    }
