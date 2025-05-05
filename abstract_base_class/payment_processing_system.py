# Create an abstract class PaymentMethod with an abstract method process_payment(). 
# Then, implement two subclasses: CreditCard and PayPal, where each subclass defines its own way to process payments. 
# The abstract class ensures that all payment methods must implement process_payment().


from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):

    @abstractmethod
    def process_payment(self, amount):
        """Abstract method to be implemented by all payment methods"""
        pass


# Subclass 1: CreditCard
class CreditCard(PaymentMethod):

    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def process_payment(self, amount):
        print(f"Processing credit card payment of ₹{amount} for card holder: {self.card_holder}")
        print(f"Card Number ending with: {self.card_number[-4:]}")
        print("Credit Card payment successful.\n")


# Subclass 2: PayPal
class PayPal(PaymentMethod):

    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        print(f"Processing PayPal payment of ₹{amount} for email: {self.email}")
        print("PayPal account charged.")
        print("PayPal payment successful.\n")


# Example usage
if __name__ == "__main__":
    payment1 = CreditCard("1234567812345678", "Jhanani")
    payment2 = PayPal("jhanani@example.com")

    payment1.process_payment(1000)
    payment2.process_payment(500)
