from simple_client import SimpleClient

if __name__ == "__main__":
    client = SimpleClient("http://localhost:8080")

    category = client.add_category("Example Category")
    print("Added Category:", category)

    categories = client.list_categories()
    print("Categories:", categories)

    product = client.add_product("Example Product", category['ID'], 100.0)
    print("Added Product:", product)

    cart_item = client.add_to_cart(product['ID'], 2)
    print("Added to Cart:", cart_item)

    payment = client.add_payment(100.0, 1)
    print("Added Payment:", payment)

    client.delete_cart_item(cart_item['ID'])
    client.delete_product(product['ID'])
    client.delete_category(category['ID'])
    client.delete_payment(payment['ID'])