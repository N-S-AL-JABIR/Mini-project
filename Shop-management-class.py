class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price


class Shop:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            self.product[product.name].quantity += product.quantity

        else:
            self.products[product.name] = product

    def buy_product(self, product_name):
        if product_name in self.products:
            qu = int(input("Tell me quantity: "))
            product = self.products[product_name]

            if product.quantity >= qu:
                product.quantity -= qu
                total = qu * product.price
                print(f"You have a ${total} bill. Please give it to me.")
                paid = int(input())

                if paid <total:
                    while True:
                        p = int(
                            input(
                                "Since the amount you paid is less than the total bill, please give me more.\n"
                            )
                        )
                        paid+=p
                        if paid>=total:
                            break

                if paid == total:
                    print("Congratulation! Here are your product")

                elif paid > total:
                    print(
                        f"Congratulation! Here are your product and the ${paid-total} return invoice."
                    )

                if product.quantity == 0:
                    del self.products[product_name]

            else:
                print(
                    f"Sorry, only {product.quantity} units of {product_name} are available."
                )
                
        else:
            print(f"Sorry, {product_name} is not available in the shop.")

    def Avaliable(self):
        if self.products:
            for product_name, product in self.products.items():
                print(
                    f"Product: {product.name}, Quantity: {product.quantity} piece(s), Price: ${product.price}"
                )
        else:
            print("No products are available in the shop.")


shop = Shop()
print("\nHey, how are you? Tell me what you'd like.")
while True:
    press = int(
        input(
            "\n   To purchase a product, press 1.\n"
            "   To add a product, press 2.\n"
            "   To see all available product, press 3.\n"
            "   To exit, press 0.\n \n"
        )
    )

    if press == 1:
        shop.buy_product(input("Enter the name of the product you want to buy: "))

    elif press == 2:
        product_name = input("Enter the name of the product to add: ")
        price = float(input(f"Enter the price of {product_name}: "))
        quantity = int(input(f"Enter the quantity of {product_name}: "))

        product = Product(product_name, quantity, price)
        shop.add_product(product)

    elif press == 3:
        shop.Avaliable()

    elif press == 0:
        print("Thank you for using the shop. Goodbye!")
        break
