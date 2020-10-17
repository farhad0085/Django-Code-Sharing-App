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
            code.author = request.user if request.user.is_authenticated else None
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


def language_page(request, language_name):

    try:
        language = Language.objects.get(name__iexact=language_name)
    except:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    codes = Code.objects.order_by('-created_utc').filter(language__name__iexact=language_name).all()
    per_page = 10
    paginator = Paginator(codes, per_page).get_page(1)

    context = {
        "language": language_name,
        "paginator": paginator
    }

    return render(request, "codes/language_specific.html", context)


def code_view(request, code_id):

    
    form = CommentForm()

    try:
        code = Code.objects.get(id=code_id)
        comments = code.comment_set.all()

    except:
        response = render(request, '404.html')
        response.status_code = 404
        return response

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.code = code

            comment.save()

            return redirect('code_view', code.id)

    else:
        code.total_views = code.total_views + 1
        code.save()

    context = {
        "code": code,
        "form": form,
        "comments": comments
    }

    return render(request, "codes/code_page.html", context)