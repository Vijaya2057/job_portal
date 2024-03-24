from django import forms
from cafe.models import Menu



class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ['name', 'price']
        widgets={
            'name':forms.TextInput(),
            'price':forms.TextInput(),
        }



 
    
