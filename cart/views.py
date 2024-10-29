# cart/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem
from digitalProducts.models import DigitalProduct  # Use DigitalProduct

@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    product_id = request.data.get('product_id')

    try:
        product = DigitalProduct.objects.get(id=product_id)
    except DigitalProduct.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    cart, created = Cart.objects.get_or_create(user=user)
    if CartItem.objects.filter(cart=cart, product=product).exists():
        return Response({'message': 'Product is already in the cart'}, status=status.HTTP_400_BAD_REQUEST)

    CartItem.objects.create(cart=cart, product=product)
    return Response({'message': 'Product added to cart'}, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def remove_from_cart(request, product_id):
    user = request.user
    cart = Cart.objects.filter(user=user).first()

    if not cart:
        return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    try:
        cart_item = CartItem.objects.get(cart=cart, product__id=product_id)
        cart_item.delete()
        return Response({'message': 'Product removed from cart'}, status=status.HTTP_200_OK)
    except CartItem.DoesNotExist:
        return Response({'error': 'Product not in cart'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user).first()

    if not cart:
        return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

    cart_items = CartItem.objects.filter(cart=cart)
    items_data = [{'product_title': item.product.title, 'added_at': item.added_at} for item in cart_items]

    return Response({'cart': items_data}, status=status.HTTP_200_OK)
