from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ["product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["id", "address", "positions"]

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        stock = super().create(validated_data)
        for pos in positions:
            stock.positions.create(**pos)
        return stock

    def update(self, instance, validated_data):
        print(validated_data)
        positions = validated_data.pop("positions")
        print(positions)
        stock = super().update(instance, validated_data)
        print(stock)
        print(instance)
        for pos in positions:
            print(pos)
            stock.positions.update_or_create(product=pos["product"], defaults={**pos})
        return stock
