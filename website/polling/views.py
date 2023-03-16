from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.timezone import datetime
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .serializers import *
from .models import *
import random

# Create your views here.

def home(request, username):
    if request.user.is_authenticated:
        if request.method == "GET":
            question = list(Question.objects.exclude(user = request.user.username).exclude(answered_by=request.user.username))
            if len(question) == 0:
                return render(request, "home.html")
            return render(request, "home.html", {"question":random.choice(question)})

        elif request.method == "POST":
            question_id = request.POST["question"]
            choice = request.POST["choice"]

            question = get_object_or_404(Question, pk=question_id)
            
            question.answered_by = request.user.username
            question.choice = choice

            try:
                question.save()

                questions = Question.objects.exclude(user = request.user.username).exclude(answered_by = request.user.username)
                if len(questions) == 0:
                    return render(request, "home.html", {"message":"No Question left to answer"})
                return render(request, "home.html", {"question": random.choice(questions)})
            except:
                return render(request, "home.html", {"message": "Try again", "question":get_object_or_404(Question, pk=question_id)})


            
    return redirect("/login/")

def question(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            return render(request, "question.html")

        elif request.method == "POST":
            username = request.user.username
            question = request.POST["question"]
            options1 = request.POST["option1"]
            options2 = request.POST["option2"]
            options3 = request.POST["option3"]
            options4 = request.POST["option4"]
            date = request.POST["date"]
            ques = Question(user = username, question=question, options1=options1, options2=options2, options3=options3, options4=options4, date=date)

            try:
                ques.save()
                return render(request, "question.html", {"message":"Saved Successfully"})
            except:
                return render(request, "question.html", {"message":"Try again"})

    return redirect("/login/")

def signup(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("mail")
        password = request.POST.get("Pass")
        first = request.POST.get("fname")
        last = request.POST.get("lname")

        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first
        user.last_name = last
        
        try:
            user.save()
            return redirect("/login/")
        except:
            return render(request, "register_page.html", {"message":"Error Occured ... try again"})

@login_required(login_url="/login/")
def userpage(request, username):
    user = get_object_or_404(User, username=username)
    questions = Question.objects.filter(user=username)
    if request.method == "GET":
        return render(request, "userpage.html", {"user": user, "questions": questions})


def Login(request):
    if request.method == "GET":
        return render(request, "login.html")

    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(f"/{user.get_username()}/")
        return render(request, "login.html", {"message": "Try again"})


def Logout(request):
    logout(request)
    return redirect("/login/")