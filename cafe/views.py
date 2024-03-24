from django.shortcuts import render
from .models import *
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from cafe.forms import MenuForm
from django.urls import reverse_lazy
from cafe.formsingre import IngredientsForm
from cafe.orderform import OrderForm



# Create your views here.
# class HomePage(View):
#     def get(self, request):
#         return render(request, 'cafe/home_page.html')


class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request,'cafe/base.html')



class MenuList(ListView):
    model=Menu
    context_object_name="menu"  #we can give object_list in place of for 
    template_name="cafe/menu_list.html"
    

class MenuCreate(CreateView):
    model=Menu
    template_name="cafe/add_menu.html"
    form_class=MenuForm 
    success_url=reverse_lazy('cafe:indexofmenu')
    

class MenuUpdate(UpdateView):
    model=Menu
    template_name="cafe/update_menu.html"
    form_class=MenuForm 
    success_url=reverse_lazy('cafe:indexofmenu')
    
class MenuDelete(DeleteView):
    model=Menu
    template_name="cafe/delete_menu.html"
    form_class=MenuForm 
    success_url=reverse_lazy('cafe:indexofmenu') 
    
    
class IngredientsList(ListView):
    model = Ingredients
    context_object_name = 'ingredients'
    template_name='cafe/ingredientslist.html'



class IngredientsCreate(CreateView):
    model=Ingredients
    template_name="cafe/add_ingredients.html"
    form_class=IngredientsForm
    success_url=reverse_lazy('cafe:indexofingredients')
    
   
class OrderList(ListView):
    model = Order
    template_name = "cafe/order_list.html"
    fields = ['order_item', 'qty', 'table_number']  # Specify the fields to include in the form
    context_object_name = 'order'



class OrderCreate(CreateView):
    model=Order
    template_name="cafe/order.html"
    form_class=OrderForm 
    success_url=reverse_lazy('cafe:indexoforder')
    
    
    
class RecipeList(ListView):
     model=Recipe
     context_object_name="recipe"
     template_name="cafe/recipe_list.html"
    
    
 
