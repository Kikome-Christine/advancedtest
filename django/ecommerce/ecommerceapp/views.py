from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from .models import Product
# Create your views here.


def submit_review(request):
    review_text = request.POST.get('review_text')
    if len(review_text) > 1000:  
        return HttpResponseBadRequest("Review too long")
     
class Payment:
    def __init__(self, amount):
        self.__amount = amount   

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        if amount > 0:
            self.__amount = amount
        else:
            raise ValueError("Amount must be positive.")
        

class PaymentProcessor:
    def process(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalProcessor(PaymentProcessor):
    def process(self, amount):
        print(f"Processing PayPal payment of ${amount}")

def process_payment(payment_processor, amount):
    payment_processor.process(amount)

 


def product_detail(request, product_id):
    # Using Django ORM's parameterized query to prevent SQL injection
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})