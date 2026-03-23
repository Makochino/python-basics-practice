class PayPal:
    def pay(self):
        return "Paid with PayPal"
    
class CreditCard:
    def pay(self):
        return "Paid with Credit Card"
    
class Crypto:
    def pay(self):
        return "Paid with Crypto"
    
def process_payment(methodic):
    print(methodic.pay())

pp, cc, crypto = PayPal(), CreditCard(), Crypto()
methods = [pp, cc, crypto]
for method in methods:
    process_payment(method)