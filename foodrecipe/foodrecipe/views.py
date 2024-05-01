from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from recipeapp.models import *



def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        ema = request.POST.get('email')
        pass_w = request.POST.get('password')
        conf_pass = request.POST.get('confirm_password')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        city = request.POST.get('city')
        country = request.POST.get('country')
        user_type = request.POST.get('user_type')

        if pass_w == conf_pass :
            user = Custom_user.objects.create_user(
                username = uname,
                email = ema,
                password = pass_w
            )
            user.Gender = gender
            user.age = age
            user.city = city
            user.country = country
            user.user_type = user_type

            user.save()

            return redirect('signin')
        else :
            return redirect('signup')

    return render(request, 'signup.html')






def signinpage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass_w = request.POST.get('password')

        user = authenticate(username = uname, password = pass_w)
        if user:
            login(request,user)
            return redirect('dashboard')
        else:
            return redirect('signin')

    return render(request,'signin.html')


def logoutpage(request):
    logout(request)
    return redirect('signin')


@login_required
def dashboardpage(request):
    
    return render(request, 'dashboard.html')


@login_required
def profilepage(request):
    current_user = request.user
    current_user_type = request.user.user_type
    if current_user_type == 'chef' :
        info = ChefModel.objects.get(myuser = current_user)
    else :
        info = ChefModel.objects.get(myuser = current_user)
    return render(request, 'profile.html',{'info': info})



@login_required
def viewrecipepage(request):
    current_user = request.user
    current_user_type = request.user.user_type
    if current_user_type == 'chef':
        info = RecipeModel.objects.filter(created_by = current_user)
    else:
        info = RecipeModel.objects.all()

    return render(request, 'viewrecipes.html',{'info': info})


@login_required
def editrecipepage(request,myid):
    info = RecipeModel.objects.get(id=myid)

    return render(request,'chef/editrecipe.html',{'info': info})


@login_required
def updaterecipe(request):

    if request.method == 'POST':
        
        rid = request.POST.get('rid')
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        preparation_time = request.POST.get('preparation_time')
        cooking_time = request.POST.get('cooking_time')
        total_time = request.POST.get('total_time')
        difficulty_level = request.POST.get('difficulty_level')
        nutrition_information = request.POST.get('nutrition_information')
        recipe_image = request.FILES.get('recipe_image')
        
        preimag = request.POST.get('recipe_ima')
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        total_calorie = request.POST.get('total_calorie')
        currect_user = request.user

        infodata = RecipeModel(
            id =rid,
            title = title,
            ingredients = ingredients,
            instructions = instructions,
            preparation_time = preparation_time,
            cooking_time = cooking_time,
            total_time = total_time,
            difficulty_level = difficulty_level,
            nutrition_information = nutrition_information,
            
            category = category,
            tags = tags,
            total_calorie = total_calorie,
            created_by = currect_user
        )
        if recipe_image:
            infodata.recipe_image = recipe_image
        else:
            infodata.recipe_image = preimag
            
        infodata.save()

        return redirect('viewrecipe')


@login_required
def deleterecipe(request,myid):
    info = RecipeModel.objects.get(id=myid)
    info.delete()
    return redirect('viewrecipe')


@login_required
def viiew(request,myid):

    info = RecipeModel.objects.get(id=myid)

    return render(request,'viiew.html',{'info': info})



@login_required
def addrecipepage(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        preparation_time = request.POST.get('preparation_time')
        cooking_time = request.POST.get('cooking_time')
        total_time = request.POST.get('total_time')
        difficulty_level = request.POST.get('difficulty_level')
        nutrition_information = request.POST.get('nutrition_information')
        recipe_image = request.FILES.get('recipe_image')
        category = request.POST.get('category')
        tags = request.POST.get('tags')
        total_calorie = request.POST.get('total_calorie')
        currect_user = request.user

        infodata = RecipeModel(
            title = title,
            ingredients = ingredients,
            instructions = instructions,
            preparation_time = preparation_time,
            cooking_time = cooking_time,
            total_time = total_time,
            difficulty_level = difficulty_level,
            nutrition_information = nutrition_information,
            recipe_image = recipe_image,
            category = category,
            tags = tags,
            total_calorie = total_calorie,
            created_by = currect_user
        )
        infodata.save()

        return redirect('viewrecipe')

    return render(request,'chef/addrecipe.html')


