from django import forms
from .models import Mesaj, Product, OrderItem


# in acest fisier vom crea clasele necesare pt a defini formulare personalizate
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price_lei', 'gramaj_ml', 'description', 'drink_type', 'nutritional_values', 'image']


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        super(OrderItemForm, self).__init__(*args, **kwargs)
        self.fields['product'].widget.attrs['class'] = 'form-control'
        self.fields['quantity'].widget.attrs['class'] = 'form-control'


class MesajForm(forms.ModelForm):
    class Meta:
        model = Mesaj
        fields = ['nume', 'prenume', 'email', 'phone', 'mesaj']