from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }

    print("USER LOGGED IN")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        context['form'] = LoginForm()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated())
        print(user)
        if user is not None:
            # print("REQUEST USER AUTHENTICATED: ", request.user.is_authenticated())
            login(request, user)
            # redirect to success page
            return redirect("/")
        else:
            # return invalid login error message
            print("ERROR")

    return render(request, "auth/login.html", context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render(request, "auth/register.html", context)


def home_page(request):
    context = {
        "title": "Home TITLE",
        "content": "home content",
    }

    if request.user.is_authenticated():
        context["premium_content"] = "YES"
    return render(request, "home_page.html", context)


def about_page(request):

    context = {
        "title": "about TITLE",
        "content": "about content"
    }
    return render(request, "home_page.html", context)


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
