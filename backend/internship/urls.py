from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_page, name="form_page"), 
    path("apply/", views.apply, name="apply"),
    path("dashboard/", views.hr_dashboard, name="hr_dashboard"),
]
