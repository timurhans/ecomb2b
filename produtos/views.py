from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from .ondas import Produto,Estoque,produtos,produtos_col,categorias
from .forms import LoginForm
import time

# Create your views here.


def product_list_view(request):

    if request.user.is_authenticated:

        try:
            col = request.GET['colecao']
            queryset = produtos_col(tabela=request.user.first_name,colecao=col)
        except:
            queryset =[]

        context = {
        'object_list' : queryset
        }

        return render(request,"produtos/lista_prods.html",context)
    else:
        print(request)
        return redirect('/login')

def product_list_view_drop(request):

    if request.user.is_authenticated:

        try:
            col = request.GET['colecao']
            queryset = produtos_col(tabela=request.user.first_name,colecao=col)
        except:
            queryset =[]
            col = ''

        paginator = Paginator(queryset, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if len(queryset)>12:
            is_paginated = True
        else:
            is_paginated = False

        cats = categorias()
        print(cats)
        context = {
        'object_list' : queryset,
        'categorias' : cats,
        'colecoes' : ['1902','2001'],
        'page_obj': page_obj,
        'is_paginated' : is_paginated,
        'selected_col' : col
        }

        return render(request,"produtos/lista_prods_drop.html",context)
    else:
        print(request)
        return redirect('/login')


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['user']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
        context = {
            'form' : form
        }

        return render(request,"produtos/login.html",context)




def logout_view(request):

    logout(request)
    return redirect('home')

