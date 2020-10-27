from django.shortcuts import render
from django import forms
from main_app.form import SignUpForm
from main_app.models import User

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def signup(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    
    return render(request, 'main/signup.html', { 'form': form })

def users(request):
    users = User.objects.order_by('first_name')
    return render(request, 'main/users.html', { 'users': users })
