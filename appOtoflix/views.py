from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "appOtoflix/home.html")

def login(request):
    return render(request, "appOtoflix/login.html")

def administrator_report(request):
    return render(request, "appOtoflix/administrator_report.html")

def configuration_menu(request):
    return render(request, "appOtoflix/configuration_menu.html")

def questions(request):
    return render(request, "appOtoflix/questions.html")

def simulated(request):
    return render(request, "appOtoflix/simulated.html")

def courses_teacher(request):
    return render(request, "appOtoflix/courses_teacher.html")

def manage_teacher(request):
    return render(request, "appOtoflix/manage_teacher.html")

def dashboard_teacher(request):
    return render(request, "appOtoflix/dashboard_teacher.html")

def administrator(request):
    return render(request, "appOtoflix/administrator.html")

def benefit_club(request):
    return render(request, "appOtoflix/benefit_club.html")

def simulated_result(request):
    return render(request, "appOtoflix/simulated_result.html")

def create_simulated(request):
    return render(request, "appOtoflix/create_simulated.html")

def questions_multiple(request):
    return render(request, "appOtoflix/questions_multiple.html")

def benefit_club_specific(request):
    return render(request, "appOtoflix/benefit_club_specific.html")

def courses_details(request):
    return render(request, "appOtoflix/courses_details.html")

def search_dashboard(request):
    return render(request, "appOtoflix/search_dashboard.html")

def courses_classes(request):
    return render(request, "appOtoflix/courses_classes.html")

def questions_inside(request):
    return render(request, "appOtoflix/questions_inside.html")