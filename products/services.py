from products.models import ProductDTO


def get_all_products():
    data = ProductDTO.objects.all()
    all_products = []
    for product in data:
        all_products.append({
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'inStock': product.inStock,
            'quantity': product.quantity,
        })

    return all_products


def create_new_product(data):
    name = data['name']
    price = data['price']
    description = data['description']
    in_stock = data['inStock']
    quantity = data['quantity']

    product = ProductDTO()
    product.name = name
    product.price = price
    product.description = description
    product.inStock = in_stock
    product.quantity = quantity
    product.save()
