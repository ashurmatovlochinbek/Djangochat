from django.http import HttpRequest
from django.shortcuts import render, redirect
from core.forms import SignUpForm
from django.contrib.auth import login



def frontpage(request: HttpRequest):
    return render(request, 'core/frontpage.html')


def signup(request: HttpRequest): 
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage') # frontpage is name of frontpage function in urls.py file in core package
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})
