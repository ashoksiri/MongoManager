from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from accounts.models import User



def render_home(request):
    return render(request,'base.html',{})

def login_view(request):


    if request.user.is_authenticated:
        return redirect('home')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'mongomanager/login.html', {'warning': 'Your acoount is Inactive'})
        else:
            return render(request, 'mongomanager/login.html', {'error': 'Invalid Username Or Password..'})

    return render(request, 'mongomanager/login.html')


def register_view(request):

    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user_data = {}
            user_data['username'] = email
            user_data['email'] = email
            user_data['password'] = password
            User.objects._create_user(**user_data)
            user = authenticate(username=email,password=password)
            if user:
                login(request, user)
                return redirect('home')
        except:
            return render(request, 'mongomanager/login.html', {'register': True, 'error': 'user already exists ...'})

def logout_view(request):
    logout(request)
    return redirect('login')
