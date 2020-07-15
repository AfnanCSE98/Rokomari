from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.db import connection
from .forms import *
from django.forms.formsets import formset_factory
import cx_Oracle

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
    conn.close()
    return customers

def Get_Cureent_Customer(all_customer , username):
    "all_customer have all the customers"
    "we return current customer from this list"
    for user in all_customer:
        if(user['NAME']==username):
            return user
def book_category(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    "First, we import the current user information"
    dict={}
    # dict['NAME'] = request.session.get('username')
    # dict["ID"] = request.session['id']
    # dict['MOBILE'] = request.session['mobile']
    # dict['EMAIL'] = request.session['email']
    # dict['ADDRESS'] = request.session['address']
    # dict['PASSWORD'] = request.session['password']
    "Now do our query"
    cursor.execute(
        '''select * from MYSELF.CATEGORY'''
    )
    res = dictfetchall(cursor)
    ctg_ID=[x['ID'] for x in res]
    ctg_NAME=[x['NAME'] for x in res]
    dict['category'] = [(x[0] , x[1]) for x in zip(ctg_ID , ctg_NAME) ]
    return render(request , 'books/book_category.html' , dict)
def Get_Author_Name(author_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select NAME from MYSELF.AUTHOR where ID=:author_id
        ''',[author_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return res[0]['NAME']

def Get_Publisher_Name(publisher_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select NAME from MYSELF.PUBLISHER where ID = :publisher_id
        ''',[publisher_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return res[0]['NAME']

def Get_Category_Name(ctg_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select NAME from MYSELF.CATEGORY where ID=:ctg_id
        ''' , [ctg_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return res[0]['NAME']

def book_category_details(request , ctg_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.BOOK where "CATEGORY ID" = :ctg_id
        ''',[ctg_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    for book in res:
        book['AUTHOR_NAME'] = Get_Author_Name(book['AUTHOR ID'])
        book['PUBLISHER_NAME'] = Get_Publisher_Name(book['PUBLISHER ID'])
    dict={}
    dict['book']=res
    dict['category_name'] = Get_Category_Name(ctg_id)
    print(dict)
    return render(request , 'books/book_category_details.html' , dict)

def book_author(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.AUTHOR 
        '''
    )
    res = dictfetchall(cursor)
    conn.close()
    author_id = [x['ID'] for x in res]
    author_name = [x['NAME'] for x in res]
    dict = {}
    dict['author'] = [(x[0], x[1]) for x in zip(author_id, author_name)]
    return render(request  , 'books/book_author.html' , dict)

def book_author_details(request , author_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.BOOK where "AUTHOR ID"=:author_id
        ''' , [author_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    for book in res:
        book['PUBLISHER_NAME'] = Get_Publisher_Name(book['PUBLISHER ID'])
        book['CATEGORY_NAME'] = Get_Category_Name(book['CATEGORY ID'])
    dict = {}
    dict['book'] = res
    dict['author_name'] = Get_Author_Name(author_id)
    print(dict)
    return render(request, 'books/book_author_details.html', dict)
def book_publisher(request ):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.PUBLISHER
        '''
    )
    res = dictfetchall(cursor)
    conn.close()
    pub_id = [x['ID'] for x in res]
    pub_name = [x['NAME'] for x in res]
    dict={}
    dict['publisher'] = [(x[0], x[1]) for x in zip(pub_id, pub_name)]
    return render(request , 'books/book_publisher.html' , dict)

def book_publisher_details(request , pub_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.BOOK where "PUBLISHER ID"=:pub_id
        ''' , [pub_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    for book in res:
        book['AUTHOR_NAME'] = Get_Author_Name(book['AUTHOR ID'])
        book['CATEGORY_NAME'] = Get_Category_Name(book['CATEGORY ID'])
    dict = {}
    dict['book'] = res
    dict['publisher_name'] = Get_Publisher_Name(pub_id)
    print(dict)
    return render(request , 'books/book_publisher_details.html' , dict)

def index(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if authenticate(username, password):

                all_customers = All_Customers()
                dict = Get_Cureent_Customer(all_customers , username)
                dict['login_message'] = "Login Successful! Welcome, "+username

                # request.session['username'] = username
                # return HttpResponseRedirect(reverse('books:home'))
                return render(request, 'books/home.html', dict)
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
            current_customer['login_message'] = "Congratulations "+username +", Sign Up Successful"
            return home(request , current_customer)
    else:
        form = UserForm()
    return render(request, 'books/signup.html', {'form': form})

def home(request ):
    username = request.session.get('username')
    dict={}
    dict['NAME'] = username
    dict['login_message'] = "Login Successful! Welcome, "+username
    print(username)
    return render(request, 'books/home.html', dict)

    # return render(request , 'books/home.html' , dict)
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
