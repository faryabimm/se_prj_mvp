from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login
from accounts.forms import SignUpForm


# Create your views here.


def login(request):
    return render(request, template_name='registration/password_reset_confirm.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # login(request=request, user=user)

            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})

