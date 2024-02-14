from django.contrib import admin
from .models import Product, Order, OrderItem, Mesaj

# in avest fisier vom inregistra modele nostre astfel incat acestea sa fie vizibile si pt a le putea gestiona din interfata Django admin
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Mesaj)

