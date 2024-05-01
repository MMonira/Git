from django.db import models
from django.contrib.auth.models import AbstractUser


class Custom_user(AbstractUser):
    GENDER=[
        ('male','male'),('female','Female'),('other','Other')
    ]
    USER = [
        ('chef','chef'),('viewer','viewer')
    ]
    Gender = models.CharField(choices=GENDER , max_length=100)
    age = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    user_type = models.CharField(choices=USER, max_length=100)


class RecipeModel(models.Model):
    LEVEL = [
        ('hard','hard'),('medium','medium'),('easy','easy')
    ]

    CATEGORY = [
        ('breakfast','breakfast'),('lunch','lunch'),('dinner','dinner')
    ]

    TAGS = [
        ('vegetarian','vegetarian'),('vegan','vegan')
    ]

    title = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    instructions = models.CharField(max_length=100)
    preparation_time = models.CharField(max_length=100)
    cooking_time = models.CharField(max_length=100)
    total_time = models.CharField(max_length=100)
    difficulty_level = models.CharField(choices= LEVEL, max_length=100)
    nutrition_information = models.CharField(max_length=100)
    recipe_image = models.ImageField(upload_to='media')
    category = models.CharField(choices= CATEGORY, max_length=100)
    tags = models.CharField(choices= TAGS, max_length=100)
    total_calorie = models.CharField(max_length=100)
    created_by = models.ForeignKey(Custom_user, on_delete=models.CASCADE,null=True)
    
    
class ChefModel(models.Model):
    myuser = models.OneToOneField(Custom_user, on_delete=models.CASCADE, null=True)
    experience = models.PositiveIntegerField(null=True)
    resume = models.FileField(null=True)
    profile_pic = models.ImageField(upload_to='media', null=True)
    skill = models.TextField( null=True)


class ViewerModel(models.Model):
    myuser = models.OneToOneField(Custom_user , on_delete=models.CASCADE, null=True)
    profile_pic = models.ImageField(upload_to='media', null=True)
    favourite = models.CharField(max_length=200, null=True)

    