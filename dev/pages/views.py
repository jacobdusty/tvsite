from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login, authenticate

from .forms import RegistrationForm

#@login_required(login_url='/accounts/login/')
def index_view(request):
    return render(request, 'pages/index.html')

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return "NOOOOO"
        # Return an 'invalid login' error message.

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    registered = False
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
        
        args = {'form': form}
        return render(request, 'pages/register.html', args)

# Create your views here.
