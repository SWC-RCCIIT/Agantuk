from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def user_login_view(request):
    form = UserRegisterForm()
    if request.method=="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request,'login.html',context)


