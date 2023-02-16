from rest_framework import serializers
from apps.main.models import Order, Customer, Cart, CartProduct, Address


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['name', 'surname', 'number', 'email']


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ['city', 'street', 'house']


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['date_ordered', 'complete', 'transaction_id']


class CartProductSerializer(serializers.ModelSerializer):

    cart = serializers.IntegerField()
    product = serializers.IntegerField()

    class Meta:
        model = CartProduct
        fields = ['cart', 'product', 'quantity']

    def validate(self, data):
        for key in data:
            if not data.get(key):
                raise serializers.ValidationError(
                    'A %s is required to order' % key
                )
        return data

    def create(self, validated_data):
        return CartProduct.objects.create(cart_id=validated_data.pop('cart'), product_id=validated_data.pop('product'), quantity=validated_data.pop('quantity'))


class OrderSerializer(serializers.Serializer):
    cart = serializers.DictField()
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=255)
    fio = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)
    street = serializers.CharField(max_length=255)
    house = serializers.CharField(max_length=255)
    customer = CustomerSerializer(many=False, read_only=True)
    address = CustomerSerializer(many=False, read_only=True)

    def validate(self, data):
        for key in data:
            if not data.get(key):
                raise serializers.ValidationError(
                    'A %s is required to order' % key
                )
        return data

    def create(self, validated_data):

        customer = {
                    'email': validated_data['email'],
                    'number': validated_data['phone'],
                    'name': validated_data['fio'].split()[0],
                    }
        try:
            customer['surname'] = validated_data['fio'].split()[1]
        except IndexError:
            customer['surname'] = None

        customer_s = CustomerSerializer(data=customer)
        customer_s.is_valid(raise_exception=True)
        customer_s.save()

        cart = Cart()
        cart.save()
        products = [{'cart': cart.id, 'product': key, 'quantity': validated_data['cart'][key]} for key in validated_data['cart']]
        products = CartProductSerializer(data=products, many=True)
        products.is_valid()
        products.save()
        # ADDRESS
        address = AddressSerializer(data={'city': validated_data['city'], 'street': validated_data['street'], 'house': validated_data['house']})
        address.is_valid(raise_exception=True)
        address.save()

        return validated_data

