from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	return render(request,'sample.html')

def sign_up(request):
    dic1 = {}
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'accounts/index.html')
    dic1['form']=form
    return render(request,'registration/sign_up.html',dic1)