import json
from unicodedata import decimal
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Expense, User, TotalAmount

# Create your views here.
amount = 0
def index(request):
    if not request.user.is_authenticated:
        return login_view(request)
    return render(request, 'tracker/index.html', {
        'totalAmount': TotalAmount.objects.get(user=request.user).totalAmount,
    })

def about(request):
    return render(request, "tracker/about.html")
@csrf_exempt
@login_required
def addMoney(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newTotalAmount = float(data["amount"])
        
        totalAmount = TotalAmount.objects.filter(user=request.user).first()
        oldTotalAmount = TotalAmount.objects.filter(user=request.user).first()
        if not totalAmount:
            totalAmount = TotalAmount(user=request.user, totalAmount=newTotalAmount)
            totalAmount.save()
        else:
            if float(oldTotalAmount.totalAmount)+newTotalAmount >= 0:
                totalAmount.totalAmount = float(oldTotalAmount.totalAmount) + newTotalAmount
                totalAmount.save()
    return JsonResponse({"message": "Amount added"})

@csrf_exempt
@login_required
def addExpense(request):
    if request.method == "POST":
        data = json.loads(request.body)
        newExpense = Expense(user=request.user, amount=float(data["amount"]), date=data["date"], description=data["description"], name=data["name"])
        totalAmount = TotalAmount.objects.filter(user=request.user).first()
        if float(totalAmount.totalAmount) - newExpense.amount < 0:
            print('Not enough money')
            return JsonResponse({"message": "Not enough money"})
        else:
            totalAmount.totalAmount = float(totalAmount.totalAmount) - newExpense.amount
            totalAmount.save()
            newExpense.save()
    return JsonResponse({"message": "Expense added"})

@login_required
def trackRecord(request):
    return render(request, "tracker/trackrecord.html", {'totalAmount': TotalAmount.objects.get(user=request.user).totalAmount})

@login_required
def getTotalAmount(request):
    try:
        totalAmount = TotalAmount.objects.get(user=request.user).totalAmount
        return JsonResponse({"totalAmount": totalAmount})
    except:
        totalAmount = 0.00
        return JsonResponse({"totalAmount": totalAmount, "message": "No total amount found"})
    
def getExpenses(request):
    expenses = Expense.objects.filter(user=request.user)
    return JsonResponse([expense.serialize() for expense in expenses], safe=False)

def login_view(request):
    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            return render(request, "tracker/login.html", {
                "message": "Invalid email and/or password."
            })
    else:
        return render(request, "tracker/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")

def register(request):
    if request.method == "POST":
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "tracker/register.html", {
                "message": "Passwords must match."
            })
        try:
            user = User.objects.create_user(email, email, password)
            user.save()
        except IntegrityError as e:
            print(e)
            return render(request, "tracker/register.html", {
                "message": "Email address already taken."
            })
        newT = TotalAmount.objects.create(user=user, totalAmount=0)
        newT.save()
        login(request, user)
        return redirect("index")
    else:
        return render(request, "tracker/register.html")
