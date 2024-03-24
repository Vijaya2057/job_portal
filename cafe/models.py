from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class Ingredients(models.Model):
    item_name = models.CharField(max_length=200)
    qty = models.IntegerField()
    unit_price = models.IntegerField()
    
    def __str__(self):
        return self.item_name
    
class Recipe(models.Model):
    name = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='recipe')
    ingredients = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    quantity = models.FloatField()    

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    order_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    qty = models.IntegerField()
    table_number = models.IntegerField()

    def __str__(self):
        return str(self.order_item)

    def update_ingredients_quantity(self):
        recipe = self.order_item.recipe.all()
        for ingredient in recipe:
            ingredient_instance = Ingredients.objects.get(item_name=ingredient.ingredients.item_name)
            ingredient_instance.qty -= ingredient.quantity * self.qty
            ingredient_instance.save()
