from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    userPhno=models.BigIntegerField()
    userPwrd=models.CharField(max_length=25)
    def get_details(self):
        return f"Username: {self.username}, Email: {self.email}, userPhno: {self.userPhno}, userPwrd: {self.userPwrd} "

class Customer(User):  
    purchase_history = models.TextField()

    def get_purchase_history(self):
        return self.purchase_history
     