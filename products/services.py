from products.models import ProductDTO, ProductInputDTO, ProductUpdateDTO


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

    product = ProductInputDTO()
    product.name = name
    product.price = price
    product.description = description
    product.inStock = in_stock
    product.quantity = quantity
    product.save()


def get_product_data(product_id):
    product = ProductDTO.objects.get(id=product_id)

    data = {
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'inStock': product.inStock,
        'quantity': product.quantity,
    }

    return data


def update_product_data(data, product_id):
    product_data = ProductDTO.objects.get(id=product_id)

    name = data['name']
    price = data['price']
    description = data['description']
    quantity = data['quantity']

    product = ProductUpdateDTO()
    product.product = product_data
    product.name = name
    product.price = price
    product.description = description
    product.quantity = quantity
    product.save()


def delete_product(product_id):
    product = ProductDTO.objects.get(id=product_id)
    product.delete()
