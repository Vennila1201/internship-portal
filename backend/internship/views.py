from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Application
from django.shortcuts import render

@csrf_exempt
def apply(request):
    if request.method == "POST":
        app = Application.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            resume=request.FILES['resume'],
            message=request.POST.get('message', '')
        )
        return JsonResponse({"message": "✅ Application submitted successfully!"})
    return JsonResponse({"error": "Invalid request"}, status=400)

def form_page(request):
    return render(request, "internship/internship.html")


def hr_dashboard(request):
    applications = Application.objects.all().order_by('-submitted_at')
    return render(request, "internship/hr_dashboard.html", {"applications": applications})