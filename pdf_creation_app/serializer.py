from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.Serializer):
    cus_address = serializers.CharField()
    email = serializers.CharField()
    phone_number = serializers.IntegerField()
    Products = [('EC4M', 'EC4M'),
                ('EC6M', 'EC6M'),
                ('EC8M', 'EC8M'),
                ('EC8MF', 'EC8MF'),
                ('EC8MF2', 'EC8MF2')]
    product = serializers.ChoiceField(choices=Products)
    MRP = serializers.CharField()
    discount = serializers.IntegerField()
    QTY = serializers.IntegerField()


class Cus(serializers.ModelSerializer):
    class Meta:
        model = Customerdetails
        fields = '__all__'
