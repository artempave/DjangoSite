from django.contrib.auth.forms import UserCreationForm, User
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .models import Articales


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            request.session['username'] = username
            return redirect('index')
        else:

            return render(request, 'main/login.html', {'error_message': 'Пользователь не найден.'})

    return render(request, 'main/login.html')

def myreg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'main/register.html', {'error_message': 'не надежный пароль, он должен состоять не меньше чем из 8 символов, содержать цифры, и заглавные буквы'})
    else:
        form = UserCreationForm()

    return render(request, 'main/register.html', {'form': form})

def index(request):
    dect = {
        'title': 'MeatBeat',
        'vales':['data', 'hi', 'ops']
        }
    data = Articales.objects.all()
    return render(request, 'main/index.html', {'data': data})

def about(request):
    return render(request, 'main/profil.html')

def setting(request):
    return render(request, 'main/setting.html')

def user_list(request):
    users = User.objects.all()
    return render(request, 'main/user_list.html', {'users': users})

# views.py

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'main/user_profil.html', {'user': user})


