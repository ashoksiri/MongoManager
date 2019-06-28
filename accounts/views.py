from django.shortcuts import render

# Create your views here.

def render_home(request):
    return render(request,'mongomanager/home.html',{})