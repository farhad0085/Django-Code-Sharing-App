from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages

def home(request):
    """
    Home Route
    """
    form =  CodeSubmissionForm()

    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Your code has been saved successfully")
            return redirect('home')

    context = {
        "form": form
    }
    
    messages.success(request, "Your code has been saved successfully")
    messages.success(request, "Your code has been saved successfully")
    messages.success(request, "Your code has been saved successfully")

    return render(request, "codes/home.html", context)