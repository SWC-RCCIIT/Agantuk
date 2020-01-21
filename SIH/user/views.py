from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def user_login_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = UserCreationForm()
        
    context = {
        'form': form
    }
    return render(request,'login.html',context)