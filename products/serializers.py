from rest_framework import serializers


class AddProductsSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(min_value=0.01, decimal_places=2, max_digits=10)
    description = serializers.CharField()
    inStock = serializers.BooleanField()
    quantity = serializers.IntegerField(min_value=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UpdateProductsSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.DecimalField(min_value=0.01, decimal_places=2, max_digits=10)
    description = serializers.CharField()
    quantity = serializers.IntegerField(min_value=0)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

