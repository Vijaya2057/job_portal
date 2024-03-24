
from django import forms
from cafe.models import Ingredients


class IngredientsForm(forms.ModelForm):
    
    class Meta:
        model = Ingredients
        fields = ['item_name', 'qty', 'unit_price']
        widgets={
            'item_name':forms.TextInput(),
            'qty': forms.TextInput(),
            'unit_price':forms.TextInput(),
        }
