from rest_framework import serializers
from .models import Dish, Table, Bill, Order

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

class BillSerializer(serializers.ModelSerializer):
    orders = OrderSerializer(many=True, read_only=True)
    orders = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='order-detail'
    )
    class Meta:
        model = Bill
        fields = ['id', 'table', 'castumername',"total_sum","is_paid","is_active", 'orders']