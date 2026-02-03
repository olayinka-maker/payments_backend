# core/models.py
from django.db import models

class PaymentDetails(models.Model):
    card1_name = models.CharField(max_length=255, blank=True)
    card1_account = models.CharField(max_length=255, blank=True)
    card2_name = models.CharField(max_length=255, blank=True)
    card2_account = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Payment Details"
