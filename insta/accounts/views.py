from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login


def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render (request,'home.html',{'form':form})



