from django.contrib import admin
from .models import Custom_user , RecipeModel , ChefModel , ViewerModel

class Custom_user_display(admin.ModelAdmin):
    list_display = ['username','email','user_type']


class recipe_display(admin.ModelAdmin):
    list_display = ['title','category','total_calorie']

admin.site.register(Custom_user,Custom_user_display)

admin.site.register(RecipeModel)
admin.site.register(ChefModel)
admin.site.register(ViewerModel)
