from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from accounts.models import User, Database
from accounts.serializers import DataBaseSeializer
from accounts.utils import  check_connection

@login_required
def render_home(request):
    return render(request,'base.html',{})

def login_view(request):


    if request.user.is_authenticated:
        return redirect('accounts:home')

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('accounts:home')
            else:
                return render(request, 'mongomanager/login.html', {'loginError': 'Your acoount is Inactive'})
        else:
            return render(request, 'mongomanager/login.html', {'loginError': 'Invalid Username Or Password..'})

    return render(request, 'mongomanager/login.html',{})


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
    return render(request,'mongomanager/signup.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

@login_required()
def profile_view(request):
    return render(request,'mongomanager/profile.html',{'page':"User Profile"})

class DatabaseView(ModelViewSet):
    queryset = Database.objects.all()
    serializer_class = DataBaseSeializer

    @action(methods=['POST'],detail=False)
    def testdb(self,request,*args,**kwargs):
        data = request.data.dict()
        data.pop('db-type')
        data.pop('csrfmiddlewaretoken')
        data.update({'port':int(data.get('port',0))})
        return Response(check_connection(**data))


@login_required
def manage_databases(request):
    context = {
        'page':'Databases',
        'databases': Database.objects.all()
    }
    return render(request,'mongomanager/manage_databases.html',context)


