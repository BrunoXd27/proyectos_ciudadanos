from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth import login, logout, authenticate
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

class Login_View(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('propuestas:propuestas_listado')
        form = AuthenticationForm()
        return render(request, 'home/login.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('propuestas:propuestas_listado')
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('propuestas:propuestas_listado')
            else:
                return render(request, 'home/login.html', {'form': form, 'error': 'Invalid credentials.'})
        return render(request, 'home/login.html', {'form': form, 'error': 'Invalid credentials.'})

class Signup_View(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('propuestas:propuestas_listado')
        form = UserCreationForm()
        return render(request, 'home/signup.html', {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('propuestas:propuestas_listado')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            ciudadano_group = Group.objects.get(name='ciudadano')
            user.groups.add(ciudadano_group)
            return redirect('home:login')
        return render(request, 'home/signup.html', {'form': form, 'error': form.errors})

class Logout_View(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('home:index')
