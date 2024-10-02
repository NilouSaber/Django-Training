from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from accounts.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomAuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username_or_email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username_or_email, password=password)
                if user is None:
                    try:
                        user = UserModel.objects.get(email=username_or_email)
                        user = authenticate(request, username=user.username, password=password)
                    except UserModel.DoesNotExist:
                        user = None
                if user is not None:
                    login(request, user)
                    return redirect('/')
            else:
                form.add_error(None, 'Error in Login')
        else:
            form = CustomAuthenticationForm()
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = CustomUserCreationForm()
        context = {'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        return redirect('/')