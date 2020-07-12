from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from .forms import *
from django.forms.formsets import formset_factory

# Create your views here.

def authenticate(username, password):
    with connection.cursor() as cursor:

        cursor.execute('''select * from "MYSELF"."CUSTOMER" where NAME=%s''', [username])
        row = cursor.fetchone()

        if row is not None:
            print(row)
            return True
        else:
            return False
def index(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if authenticate(username, password):
                return render(request, 'books/home.html', {'username': username})
            else:
                form = LoginForm()
                return render(request, 'books/index.html', {'form': form})
    else:
        form = LoginForm()
        return render(request , 'books/index.html' , {'form':form})


def CreateCustomer(username , email , mobile , address):

    with connection.cursor() as cursor:

        cursor.execute('''
                        INSERT INTO "MYSELF"."CUSTOMER"(ID , MOBILE , ADDRESS , EMAIL ,  NAME)
                        VALUES(25 ,%s , %s , %s , (%s))
                        ''' ,
                       [mobile , address , email , username])

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            mobile  =form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            CreateCustomer( username, email, mobile, address)


            #request.session['username'] = username
            # return HttpResponseRedirect(reverse('books:home'))
            return render(request , 'books/home.html' , {'username':username})
    else:
        form = UserForm()
    return render(request, 'books/signup.html', {'form': form})

# def home(request):
#     if request.session.has_key('username'):
#         username = request.session.get('username')
#         print("hi")
#         return render(request, 'books/home.html', {'username': username})
#     else:
#         print("home session not found")
#         # form = LoginForm()
#         # return render(request, 'books/index.html' , {'form':form})
#         # # return index(request)
