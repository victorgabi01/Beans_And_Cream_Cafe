from django.db import models
from django.conf import settings


# aici vom defini modele pt structura bazei de date

class Product(models.Model):
    name = models.CharField(max_length=200)
    price_lei = models.DecimalField(max_digits= 10, decimal_places=2, default= 0)
    gramaj_ml = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    description = models.TextField()
    drink_type = models.TextField(default=0)
    nutritional_values = models.TextField(default=0)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)


    def __str__(self):
        return self.name


class OrderItem(models.Model): # clasa cu ajutorul caruia definim caracteristicile si comportamentul pt unul sau mai multe produse dint-o comanda
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self): # acesta metota ne retuneaza cantitatea totala a unui produs
        return self.quantity * self.product.price_lei

    def get_final_price(self): # acesta metota ne retuneaza valoarea totala a unui produs dintr-o comanda
        return self.get_total_item_price()


class Order(models.Model): # clasa cu ajutorul caruia definim caracteristicile si comportamentul unei comenzi
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} - {self.user.username}"

    def get_total(self):  # acesta metota ne retuneaza valoarea totala a comenzii
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total


class Mesaj(models.Model): #clasa cu ajutorul caruia definim caracteristicile unui mesaj primit de la utilizator
    STATUS_CHOICES = [
        ('necitit', 'Necitit'),
        ('rezolvat', 'Rezolvat'),
    ]

    nume = models.CharField(max_length=100)
    prenume = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    mesaj = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='necitit')
    data_inregistrare = models.DateTimeField(auto_now_add=True)
