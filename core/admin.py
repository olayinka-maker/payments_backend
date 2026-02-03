
# core/admin.py
from django.contrib import admin
from .models import PaymentDetails

@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('card1_name', 'card1_account', 'card2_name', 'card2_account', 'updated_at')
