from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):

    form =  CodeSubmissionForm()

    if request.method == "POST":
        form = CodeSubmissionForm(request.POST)

        if form.is_valid():
            code = form.save(commit=False)
            code.author = request.user
            code.save()

            messages.success(request, "Your code has been saved successfully")
            return redirect('code_view', code.id)

    # latest 10 public code snippet
    codes = Code.objects.order_by('-created_utc').all()
    per_page = 10
    paginator = Paginator(codes, per_page).get_page(1)

    context = {
        "form": form,
        "codes": codes,
        "paginator": paginator
    }

    return render(request, "codes/home.html", context)

def code_view(request, code_id):
    code = Code.objects.get(id=code_id)
    code.total_views = code.total_views + 1
    code.save()

    context = {
        "code": code,
    }

    return render(request, "codes/code_page.html", context)