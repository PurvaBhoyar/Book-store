def cart_items(request):
    cart = request.session.get('cart', {})
    return {'cart_item_count': len(cart)}