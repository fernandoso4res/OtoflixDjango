from django.contrib import admin
from django.urls import path
from appOtoflix.views import home, login, administrator_report, configuration_menu, questions, simulated, courses_teacher, manage_teacher, dashboard_teacher, administrator, benefit_club, simulated_result, create_simulated, questions_multiple, benefit_club_specific, courses_details, search_dashboard, courses_classes, questions_inside

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('login/', login),
    path('administrator-report/', administrator_report),
    path('configuration-menu/', configuration_menu),
    path('questions/', questions),
    path('simulated/', simulated),
    path('courses-teacher/', courses_teacher),
    path('manage-teacher/', manage_teacher),
    path('dashboard-teacher/', dashboard_teacher),
    path('administrator/', administrator),
    path('benefit-club/', benefit_club),
    path('simulated-result/', simulated_result),
    path('create-simulated/', create_simulated),
    path('questions-multiple/', questions_multiple),
    path('benefit-club-specific/', benefit_club_specific),
    path('courses_details/', courses_details),
    path('search-dashboard/', search_dashboard),
    path('courses-classes/', courses_classes),
    path('questions-inside/', questions_inside)
]
