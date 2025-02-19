from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_user(request):
    """
    View to register a new user.

    This view handles the user registration process. If the request method is POST, 
    the form is validated and the user is created. Upon successful registration, 
    the user is automatically logged in and redirected to the posts list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered registration form template or a redirect to the posts list page.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Register the user and log them in automatically
            login(request, form.save())
            return redirect("posts:posts")  # Redirect to the posts list page after registration
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {"form": form})

def login_user(request):
    """
    View to log in an existing user.

    This view handles the login process. If the request method is POST, the form is validated 
    and the user is authenticated. Upon successful login, the user is redirected to the 'next' 
    page if provided, otherwise, they are redirected to the posts list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered login form template or a redirect to the posts list page.
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            login(request, form.get_user())
            # Redirect to the next page if available, otherwise go to the posts list
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("posts:posts")
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {"form": form})

def logout_user(request):
    """
    View to log out the current user.

    This view handles the logout process. When a POST request is made, the user is logged out 
    and redirected to the posts list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A redirect to the posts list page after logging out.
    """
    if request.method == "POST":
        logout(request)
        return redirect("posts:posts")  # Redirect to the posts list page after logging out
