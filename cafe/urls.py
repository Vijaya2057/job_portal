
from django.contrib import admin
from django.urls import path




from .import views
app_name="cafe"
urlpatterns=[
        
        path('home/',views.Base.as_view(),name='base'),
        path('menulist/', views.MenuList.as_view(),name="indexofmenu"),
        path('menuadd/', views.MenuCreate.as_view(),name='menucreate'),
        # path('home/',HomePage.as_view(),name='home_page'),
        path('ingrelist/', views.IngredientsList.as_view(),name="indexofingredients"),
        path('ingreadd/', views.IngredientsCreate.as_view(),name='ingredientscreate'),
        
        path('orderlist/', views.OrderList.as_view(),name="indexoforder"),
        path('orderadd/', views.OrderCreate.as_view(),name='orderadd'),
        
        path('recipelist/', views.RecipeList.as_view(),name="indexofrecipe"),
        
        
        
        


]





   



