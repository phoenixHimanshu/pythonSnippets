from abc import ABC, abstractmethod

class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod 
    def pay(self, order, security_code):
        pass

class DebitPaymentGateway(PaymentProcessor):
  
    def __init__(self,security_code) -> None:
        self.security_code = security_code

    def pay(self, order ):  #security code is set in constructor
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class CreditPaymentGateway(PaymentProcessor):

    def __init__(self,security_code) -> None:
        self.security_code = security_code
      
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"

class PaypalPaymentGateway(PaymentProcessor):
    def __init__(self, email) -> None:
        self.email = email

    def pay(self, order):
        print("Processing debit payment type")
        print(f"Email for paypal payment: {self.email}")
        order.status = "paid"

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)

print(order.total_price())
processor = PaypalPaymentGateway( "phoenix_heman@gmail.com") # email is set in constructor
processor.pay(order) # call with orders only
