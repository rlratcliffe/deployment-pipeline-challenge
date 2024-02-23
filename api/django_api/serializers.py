from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('trace_id', 'abbreviated_name', 'food_ordered', 'started_status', 'processing_status')