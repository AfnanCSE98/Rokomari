from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from .forms import *
from django.forms.formsets import formset_factory
import cx_Oracle
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rokomari.settings')

django.setup()

# Create your views here.
def Max_CustomerID():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    try:
        cursor.execute('''select MAX(ID)
                    from "MYSELF"."CUSTOMER" ''')

    except cx_Oracle.Error as e:
        print(e)


    res=cursor.fetchall()
    print(res[0][0])
    conn.close()
    return res[0][0]

def authenticate(username, password):
    with connection.cursor() as cursor:

        cursor.execute('''select * from "MYSELF"."CUSTOMER" where NAME=%s''', [username])
        row = dictfetchall(cursor)
        for user in row:
            if(user['PASSWORD']==password):
                return True
        return False

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
def All_Customers():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                        select * from MYSELF.CUSTOMER
                        ''')
    customers = dictfetchall(cursor)
    # print(len(customers))
    # for user in customers:
    #     print(user['NAME'])
    conn.close()
    return customers
def Get_Cureent_Customer(all_customer , username):
    "all_customer have all the customers"
    "we return current customer from this list"
    for user in all_customer:
        if(user['NAME']==username):
            return user

def index(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if authenticate(username, password):
                all_customers = All_Customers()
                current_customer = Get_Cureent_Customer(all_customers , username)
                current_customer['login_message'] = "Login Successful! Congratulations"
                return render(request, 'books/home.html', current_customer)
            else:
                form = LoginForm()
                dict = {}
                dict['login_message'] = "Login Failed! Sorry"
                dict['form'] = form
                return render(request, 'books/index.html', dict)
    else:
        form = LoginForm()
        return render(request , 'books/index.html' , {'form':form})


def CreateCustomer(id,username , email , mobile , address , password):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO MYSELF.CUSTOMER(ID , MOBILE , ADDRESS , EMAIL ,  NAME , PASSWORD)
                    VALUES(:id,:mobile,:address,:email,:username,:password )
                    ''',[id, mobile, address, email, username , password])
    conn.commit()
    conn.close()

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            mobile  = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            id = Max_CustomerID()
            id = id+1
            CreateCustomer(id, username, email, mobile, address , password)

            all_customers = All_Customers()
            current_customer = Get_Cureent_Customer(all_customers, username)
            current_customer['login_message'] = "Congratulations! Sign Up Successful"
            return render(request , 'books/home.html' , current_customer)
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
