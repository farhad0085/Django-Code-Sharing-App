from django.shortcuts import render

def home(request):
    """
    Home Route
    """
    return render(request, "codes/home.html")