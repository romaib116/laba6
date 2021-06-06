from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AstroRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def text_page(request):
    return render(request, 'main/text_page.html', {'title': 'Кармическая задача'})


def tabl_page(request):
    return render(request, 'main/tabl_page.html', {'title': 'Знаки зодиака'})


@login_required(login_url='login')
def form_page(request):
    error= ''
    if request.method == "POST":
        form = AstroRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is error'
    form = AstroRegisterForm()
    context = {
        'title': 'Помощь астролога',
        'form': form,
        'error': error
    }
    return render(request, 'main/form_page.html', context)


def login_user(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            form_data = login_form.cleaned_data
            user = authenticate(username=form_data['username'], password=form_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    request.session['user'] = form_data['username']
                    response = redirect('home')
                    response.set_cookie(
                        'AuthToken',
                        request.session['user'],
                        max_age=None,
                        domain=None,
                        secure=False,
                    )
                    return response
                else:
                    return HttpResponse('Disabled account')
            else:
                return redirect('register')
        else:
            return HttpResponse(str(login_form.errors))
    elif request.method == 'GET':
        login_form = AuthenticationForm()
        return render(request, 'main/login.html', {'title': 'LOGIN', 'login_form': login_form })


def register_user(request):
    if request.method == "POST":
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            return redirect('login')
        else:
            return HttpResponse(str(register_form.errors))
    elif request.method == 'GET':
        register_form = UserCreationForm()
        return render(request, 'main/register.html', { 'title': 'Register', 'register_form': register_form })

