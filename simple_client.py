import requests


class SimpleClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def add_category(self, name):
        response = requests.post(f"{self.base_url}/categories", json={"name": name})
        return response.json()

    def list_categories(self):
        response = requests.get(f"{self.base_url}/categories")
        return response.json()

    def get_category(self, category_id):
        response = requests.get(f"{self.base_url}/categories/{category_id}")
        return response.json()

    def delete_category(self, category_id):
        response = requests.delete(f"{self.base_url}/categories/{category_id}")
        return response.status_code

    def add_product(self, name, category_id, price):
        response = requests.post(f"{self.base_url}/products",
                                 json={"name": name, "category_id": category_id, "price": price})
        return response.json()

    def list_products(self):
        response = requests.get(f"{self.base_url}/products")
        return response.json()

    def get_product(self, product_id):
        response = requests.get(f"{self.base_url}/products/{product_id}")
        return response.json()

    def delete_product(self, product_id):
        response = requests.delete(f"{self.base_url}/products/{product_id}")
        return response.status_code

    def update_product(self, product_id, name, category_id, price):
        response = requests.put(f"{self.base_url}/products/{product_id}",
                                json={"name": name, "category_id": category_id, "price": price})
        return response.json()

    def add_to_cart(self, product_id, quantity):
        response = requests.post(f"{self.base_url}/cart", json={"productID": product_id, "quantity": quantity})
        return response.json()

    def list_cart_items(self):
        response = requests.get(f"{self.base_url}/cart")
        return response.json()

    def update_cart_item(self, cart_item_id, product_id, quantity):
        response = requests.put(f"{self.base_url}/cart/{cart_item_id}",
                                json={"productID": product_id, "quantity": quantity})
        return response.json()

    def delete_cart_item(self, cart_item_id):
        response = requests.delete(f"{self.base_url}/cart/{cart_item_id}")
        return response.status_code

    # Payment Endpoints
    def list_payments(self):
        response = requests.get(f"{self.base_url}/payments")
        return response.json()

    def add_payment(self, amount, order_id):
        response = requests.post(f"{self.base_url}/payments", json={"amount": amount, "order_id": order_id})
        return response.json()

    def get_payment(self, payment_id):
        response = requests.get(f"{self.base_url}/payments/{payment_id}")
        return response.json()

    def delete_payment(self, payment_id):
        response = requests.delete(f"{self.base_url}/payments/{payment_id}")
        return response.status_code
