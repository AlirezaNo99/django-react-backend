# cart/views.py
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem
from digitalProducts.models import DigitalProduct  # Use DigitalProduct

@api_view(['POST'])
def add_to_cart(request):
    user = request.user
    print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}, Type: {type(request.user)}")
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 1))

    if quantity < 1:
        return Response({'error': 'Quantity must be at least 1'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        product = DigitalProduct.objects.get(id=product_id)
    except DigitalProduct.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    cart, created = Cart.objects.get_or_create(user=user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += quantity  # Update quantity if item already exists
        cart_item.save()

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
    
    items_data = [
        {
            'product_id': item.product.id,
            'product_mainPic': item.product.mainPic.url if item.product.mainPic else None,
            'product_title': item.product.title, 
            'product_price': item.product.price, 
            'quantity': item.quantity,
            'added_at': item.added_at
        }
        for item in cart_items
    ]
    
    # Calculate the total price of the cart
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    return Response({
        'cart': items_data,
        'total_price': total_price  # Include the total price
    }, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update_cart_item(request, product_id):
    user = request.user
    quantity = int(request.data.get('quantity', 1))

    if quantity < 1:
        return Response({'error': 'Quantity must be at least 1'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        cart_item = CartItem.objects.get(cart__user=user, product_id=product_id)
        cart_item.quantity = quantity
        cart_item.save()
        return Response({'message': 'Cart item quantity updated'}, status=status.HTTP_200_OK)

    except CartItem.DoesNotExist:
        return Response({'error': 'Product not in cart'}, status=status.HTTP_404_NOT_FOUND)