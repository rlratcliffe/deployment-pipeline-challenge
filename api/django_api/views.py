from django.shortcuts import render
from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order

class OrderView(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()