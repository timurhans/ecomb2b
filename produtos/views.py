from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth import authenticate, login, logout
from .ondas import (Produto,Estoque,produtos,
produtos_col,categorias,produtos_col_cat,subcategorias,
produtos_col_cat_subcat,cats_subcats)
from .forms import LoginForm
import time

# Create your views here.


def home_view(request):

    if request.user.is_authenticated:

        context = {
        'colecoes' : ['1902','2001']
        }

        return render(request,"produtos/home.html",context)
    else:
        print(request)
        return redirect('/login')

def colecao_view(request,colecao):

    if request.user.is_authenticated:
        cats = categorias()
        context = {
        'categorias' : cats
        }

        return render(request,"produtos/colecao.html",context)
    else:
        print(request)
        return redirect('/login')

def categoria_view(request,colecao,categoria):

    if request.user.is_authenticated:
        cats = subcategorias(categoria)
        context = {
        'subcategorias' : cats
        }

        return render(request,"produtos/categoria.html",context)
    else:
        print(request)
        return redirect('/login')


def product_list_view(request,colecao,categoria,subcategoria):

    if request.user.is_authenticated:


        queryset = produtos_col_cat_subcat(tabela=request.user.first_name,
        colecao=colecao,categoria=categoria,subcategoria=subcategoria)


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
            cat = request.GET['categoria']
            queryset = produtos_col_cat(tabela=request.user.first_name,
                colecao=col,categoria=cat)
            try:
                subcat = request.GET['subcategoria']
                queryset = produtos_col_cat_subcat(tabela=request.user.first_name,
                colecao=col,categoria=cat,subcategoria=subcat)
            except:
                queryset = produtos_col_cat(tabela=request.user.first_name,
                colecao=col,categoria=cat)
                subcat = ''
            
        except:
            queryset =[]
            col = ''
            cat = ''
            subcat = ''

        paginator = Paginator(queryset, 12)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if len(queryset)>12:
            is_paginated = True
        else:
            is_paginated = False

        cats = cats_subcats()
        context = {
        'object_list' : queryset,
        'categorias' : cats,
        'colecoes' : ['1902','2001'],
        'page_obj': page_obj,
        'is_paginated' : is_paginated,
        'selected_col' : col,
        'selected_cat' : cat,
        'selected_subcat' : subcat
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

