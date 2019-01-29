from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model

from .forms import ContactForm


def home_page(request):
    print(request.session.get("first_name", "unknown"))
    context = {
        "title": "MEMullinArt",
        "desc": "Watercolor Prints & Notecards",
        "content": "home content",
    }

    if request.user.is_authenticated:
        context["premium_content"] = "YES"
    return render(request, "home_page.html", context)


def about_page(request):

    context = {
        "title": "About The Artist",
        "content": "About the Artist"
    }

    return render(request, "about.html", context)


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "contact TITLE",
        "content": "contact content",
        "form": contact_form

    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # if request.method == "POST":
    #     print(request.POST.get("fullname"))
    #     print(request.POST.get("email"))
    #     print("We have content:", request.POST.get("content"))

    return render(request, "contact/view.html", context)
