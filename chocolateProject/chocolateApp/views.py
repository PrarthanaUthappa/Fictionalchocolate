
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Flavors,Ingredients,Customer_Feedback
# from database import init_db,addSeasonal_flavors,Update_Ingredients,Customer_Feedback
# //db initialization
# init_db()

def ind(request):
    # Fetch all flavors
    flavors = Flavors.objects.all()
    # Fetch all ingredients (if you need to display them)
    ingredients = Ingredients.objects.all()
    # Fetch all feedback (if you need to display them)
    feedbacks = Customer_Feedback.objects.all()
    
    # Pass the data to the template
    context = {
        'flavors': flavors,
        'ingredients': ingredients,
        'feedbacks': feedbacks,
    }
    return render(request,'chocolateApp/ind.html',context)

def addFlavor(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Season=request.POST['Season']
        Price=request.POST['Price']
        flavor=Flavors(Name=Name,Season=Season,Price=Price)
        flavor.save()
        return redirect('ind')
    else:
        return render(request,'chocolateApp/add_flavor.html')

def update_ing(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Quantity=request.POST['Quantity']
        Expiry=request.POST['Expiry']
        ing=Ingredients(Name=Name,Quantity=Quantity,Expiry=Expiry)
        ing.save()
        return redirect('ind')
    else:
        return render(request, 'chocolateApp/update_ing.html')


def customer_feedback(request):
    if request.method=='POST':
        Flavor_suggestion=request.POST['Flavor_suggestion']
        Allergy_concerns=request.POST['Allergy_concerns']
        CB=Customer_Feedback(Flavor_suggestion=Flavor_suggestion,Allergy_concerns=Allergy_concerns)
        CB.save()
        return redirect('ind')
    else:
        return render(request, 'chocolateApp/cust_FB.html')
    
def list_all(request):
    # Fetch all flavors, ingredients, and feedback
    flavors = Flavors.objects.all()
    ingredients = Ingredients.objects.all()
    feedbacks = Customer_Feedback.objects.all()
    
    # Pass the data to the template
    context = {
        'flavors': flavors,
        'ingredients': ingredients,
        'feedbacks': feedbacks,
    }
    
    return render(request, 'chocolateApp/list_all.html', context)



