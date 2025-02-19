from django.shortcuts import render

# View for the homepage
def homepage(request):
    """
    View to render the homepage.
    
    This view is responsible for rendering the 'home.html' template 
    which serves as the main landing page of the application.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered homepage template.
    """
    # return HttpResponse("Hello World! I am home page.")  # Alternative for a simple response
    return render(request, 'home.html')

# View for the about page
def aboutpage(request):
    """
    View to render the about page.
    
    This view is responsible for rendering the 'about.html' template 
    which provides information about the application.
    
    Args:
        request (HttpRequest): The HTTP request object.
        
    Returns:
        HttpResponse: The rendered about page template.
    """
    # return HttpResponse("Hello, I am about page.")  # Alternative for a simple response
    return render(request, 'about.html')
