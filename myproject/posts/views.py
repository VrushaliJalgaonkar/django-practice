from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def posts_list(request):
    """
    View to display the list of all posts.

    This view retrieves all posts from the database, orders them by date 
    in descending order, and renders the 'posts_list.html' template 
    to display the list of posts.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered posts list template with posts.
    """
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', {'posts': posts})

def post_page(request, slug):
    """
    View to display a single post page.

    This view retrieves a single post based on the given slug 
    and renders the 'post_page.html' template to display the post's content.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the post to retrieve.

    Returns:
        HttpResponse: The rendered post page template with the post.
    """
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post_page.html', {'post': post})

@login_required(login_url="/users/login/")
def posts_new(request):
    """
    View to create a new post.

    This view displays a form to create a new post. The user must be logged in 
    to access this view. Upon successful form submission, the post is saved 
    with the current user as the author, and the user is redirected to the 
    posts list page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered new post form template or a redirect to the posts list.
    """
    if request.method == "POST":
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user  # Assigning the logged-in user as the author
            newpost.save()
            return redirect('posts:posts')  # Redirect to the posts list page
    else:
        form = forms.CreatePost()

    return render(request, 'posts/new_post.html', {'form': form})
