from django.shortcuts import redirect, render
from django.http import JsonResponse

# import all your forms to be used
from .forms import PostForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm

# import all your models to be used
from .models import Post

# import extra functionality (authenticate/login/logout/ and messages)
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

# import mail dependencies
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    # return HttpResponse("Hello, world! This is the blog index ;]")
    #
    # instead of returning an http response, we are rendering a template
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')

@login_required(login_url='blog-login')
def createPost(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form' : form
    }
    return render(request, 'blog/createpost.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('blog-index')
    form = CreateUserForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")

        print(settings.EMAIL_HOST_USER)
        print(settings.EMAIL_HOST_PASSWORD)

        template = render_to_string('blog/emailtemplate.html', {'username' : user})

        email_message = EmailMessage(
            'Welcome to my Django Blog!', # subject line
            template, # body
            settings.EMAIL_HOST_USER,
            [email], #list of recipients
            fail_silently = False
        )

        email_message.send()

        messages.success(request, "Account was created for " + user)
        return redirect('blog-login')
    context = {
        'form' : form
    }
    return render(request, 'blog/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('blog-index')
    if request.method == "POST":
        username = request.POST.get('username') # comes from name attribute in html input tag
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog-index')
        messages.info(request, "Incorrect username OR password")
    return render(request, 'blog/login.html')

def logoutUser(request):
    logout(request)
    return redirect('blog-login')

def testAPI(request):
    return JsonResponse(
        {
            "name": "Launch-1",
            "students": ['Chien', 'Dan', "Jerry", "Jerry", "Koki", "Olivia", "Peter", "Young"],
        }
    )
