from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from django.shortcuts import redirect
from django.forms.formsets import formset_factory
import cx_Oracle

# Create your views here.

def Max_CustomerID():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute('''select MAX(ID)
                from "MYSELF"."USER" ''')

    res=cursor.fetchall()
    print(res)
    conn.close()
    if type(res[0][0]) == type(None):
        return 0
    else:
        return res[0][0]


def Max_OrderID():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute('''select MAX(ORDER_ID)
                    from "MYSELF"."ORDER_HISTORY" ''')

    res = cursor.fetchall()
    print(res)
    conn.close()
    if type(res[0][0]) == type(None):
        return 0
    else:
        return res[0][0]


def Max_Rating():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute('''select MAX(ID)
                        from "MYSELF"."RATING" ''')
    res = cursor.fetchall()
    conn.close()
    if type(res[0][0]) == type(None):
        return 0
    else:
        return res[0][0]


def Max_Comment():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute('''select MAX(ID)
                            from "MYSELF"."COMMENT" ''')
    res = cursor.fetchall()
    conn.close()
    if type(res[0][0]) == type(None):
        return 0
    else:
        return res[0][0]


def authenticate(username, password):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''select * from "MYSELF"."USER" where NAME=:username''', [username])
    row = dictfetchall(cursor)
    conn.close()
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


def All_Users():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                        select * from "MYSELF"."USER" 
                        ''' )
    customers = dictfetchall(cursor)
    conn.close()
    return customers


def Get_Current_Customer(all_customer , username):
    "all_customer have all the customers"
    "we return current customer from this list"
    for user in all_customer:
        print(user)
        if(user['NAME']==username):
            return user


def book_category(request):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        dict={}
        cursor.execute(
            '''select * from MYSELF.CATEGORY'''
        )
        res = dictfetchall(cursor)
        conn.close()
        ctg_ID=[x['ID'] for x in res]
        ctg_NAME=[x['NAME'] for x in res]
        dict['category'] = [(x[0] , x[1]) for x in zip(ctg_ID , ctg_NAME)]
        "storing current customer information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['none'] = None
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request , 'books/book_category.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'books/index.html', {'form': form})


def Get_Author_Name(author_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select NAME from MYSELF.AUTHOR where ID=:author_id
        ''', [author_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return res[0]['NAME']


def GET_ORDER_STATUS(order_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select STATUS from "MYSELF"."ORDER_HISTORY" where ORDER_ID=:order_id
        ''', [order_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return res[0]['STATUS']

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
        ''', [ctg_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return res[0]['NAME']


def Get_Book_Name_Price(book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select TITLE, PRICE from MYSELF.BOOK where "BOOK ID"=:book_id
        ''', [book_id]
    )
    res = dictfetchall(cursor)
    conn.close()
    return book_id, res[0]['TITLE'], res[0]['PRICE']


def Get_Cart(customer_id, order_id = -1):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''select ID, QUANTITY from "MYSELF"."CART" where "CUSTOMER ID" =:customer_id AND "ORDER_ID" =:order_id
                            ''', [customer_id, order_id])
    res = dictfetchall(cursor)
    conn.close()
    return res

def Get_Order_IDs(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    select "ORDER_ID" from "MYSELF"."ORDER_HISTORY"
                    where "CUSTOMER_ID" =:customer_id''',
                        [customer_id])
    res = dictfetchall(cursor)
    conn.close()
    return res

def getCustomerName(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM "MYSELF"."USER"
                        WHERE ID =: customer_id''', { 'customer_id' : customer_id})
    res = dictfetchall(cursor)
    conn.close()
    if len(res):
        return res[0]['NAME']
    else:
        return None

def getCustomerRating(customer_id, book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT STARS FROM "MYSELF"."RATING"
                    WHERE "CUSTOMER ID" =: customer_id AND "BOOK ID" =: book_id''',
                   {'customer_id': customer_id , 'book_id' : book_id})
    res = dictfetchall(cursor)
    conn.close()
    if len(res):
        return res[0]['STARS']
    else:
        return None

def getAverageRating(book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT "STARS" FROM "MYSELF"."RATING"
                        WHERE "BOOK ID" =: book_id''', { 'book_id' : book_id})
    res = dictfetchall(cursor)
    conn.close()
    sum = 0;
    len = 0;
    for item in res:
        sum += item['STARS']
        len += 1
    if sum == 0:
        return None
    else:
        return (sum/len)

def getComment(book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."COMMENT"
                        WHERE "BOOK ID" =: book_id''', { 'book_id' : book_id})
    res = dictfetchall(cursor)
    conn.close()
    lst = []
    for item in res:
        lst.append((int(item['ID']), item['DESCRIPTION'], getCustomerName(item['CUSTOMER ID'])))
        print(item['CUSTOMER ID'])
    lst.sort(reverse=True)
    return lst

def delete_Cart_Item(request, book_id):
    customer_id = request.session.get('id')
    print(book_id + " " + str(customer_id))
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''delete from "MYSELF"."CART" where "ID" =:book_id and "CUSTOMER ID" =:customer_id
                        ''', {'book_id' : book_id, 'customer_id' : customer_id})
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/cart/')

def book_category_details(request , ctg_id, book_id = None):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.BOOK where "CATEGORY ID" = :ctg_id
            ''', [ctg_id]
        )
        res = dictfetchall(cursor)
        customer_id = request.session['id']
        if book_id:
            print(book_id)
            quantity = -1
            order_id = -1
            cursor.execute('''
                               INSERT INTO "MYSELF"."CART"("ID", "CUSTOMER ID", "QUANTITY", "ORDER_ID")
                               VALUES(:book_id, :customer_id, :quantity, :order_id)
                               ''', [book_id, customer_id, quantity, order_id])
            conn.commit()
        conn.close()
        for book in res:
            book['ID'] = book['BOOK ID']
            book['AUTHOR_NAME'] = Get_Author_Name(book['AUTHOR ID'])
            book['PUBLISHER_NAME'] = Get_Publisher_Name(book['PUBLISHER ID'])
        dict = {}
        dict['book'] = res
        dict['category_name'] = Get_Category_Name(ctg_id)
        dict['category_id'] = ctg_id
        "Storing current customer information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request, 'books/book_category_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'books/index.html', {'form': form})


def book_author(request):
    if request.session.has_key('username'):
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

        "Storing current customer information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request  , 'books/book_author.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'books/index.html', {'form': form})


def book_author_details(request , author_id, book_id = None):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.BOOK where "AUTHOR ID"=:author_id
            ''', [author_id]
        )
        res = dictfetchall(cursor)
        customer_id = request.session['id']
        if book_id:
            print(book_id)
            cursor = conn.cursor()
            cursor.execute('''
                               INSERT INTO "MYSELF"."CART"("ID", "CUSTOMER ID")
                               VALUES(:book_id, :customer_id)
                               ''', [int(book_id), customer_id])
            conn.commit()
        conn.close()
        for book in res:
            book['ID'] = book['BOOK ID']
            book['PUBLISHER_NAME'] = Get_Publisher_Name(book['PUBLISHER ID'])
            book['CATEGORY_NAME'] = Get_Category_Name(book['CATEGORY ID'])
        dict = {}
        dict['book'] = res
        dict['author_name'] = Get_Author_Name(author_id)

        "Storing current customer information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['author_id'] = author_id
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request, 'books/book_author_details.html', dict)

    else:
        form = LoginForm()
        return render(request, 'books/index.html', {'form': form})


def book_publisher(request ):
    if request.session.has_key('username'):
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
        "Storing current user information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request , 'books/book_publisher.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'books/index.html', {'form': form})


def book_publisher_details(request , pub_id, book_id=None):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.BOOK where "PUBLISHER ID"=:pub_id
            ''', [pub_id]
        )
        res = dictfetchall(cursor)
        customer_id = request.session['id']
        if book_id:
            print(book_id)
            cursor = conn.cursor()
            cursor.execute('''
                                       INSERT INTO "MYSELF"."CART"("ID", "CUSTOMER ID")
                                       VALUES(:book_id, :customer_id)
                                       ''', [int(book_id), customer_id])
            conn.commit()
        conn.close()
        for book in res:
            book['ID'] = book['BOOK ID']
            book['AUTHOR_NAME'] = Get_Author_Name(book['AUTHOR ID'])
            book['CATEGORY_NAME'] = Get_Category_Name(book['CATEGORY ID'])
        dict = {}
        dict['book'] = res
        dict['publisher_name'] = Get_Publisher_Name(pub_id)
        "Storing current user information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['publisher_id'] = pub_id
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request, 'books/book_publisher_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'books/index.html', {'form': form})


def cart(request):
    dict={}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = len(Get_Cart(request.session.get('id')))
    res = Get_Cart(dict['id'])
    lst = []
    for item in res:
        lst.append(Get_Book_Name_Price(item['ID']))
    dict['cart'] = lst
    print(dict['cart'])
    total = 0
    for a, b, c in dict['cart']:
        total += int(c)
    dict['total'] = total
    return render(request, 'books/cart.html', dict)


def index(request):
    if request.method=="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if authenticate(username, password):
                all_customers = All_Users()
                dict = Get_Current_Customer(all_customers , username)
                print(username)
                request.session['username'] = dict['NAME']
                request.session['id'] = dict["ID"]
                request.session['mobile'] = dict['MOBILE']
                request.session['email'] = dict['EMAIL']
                request.session['address'] = dict['ADDRESS']
                request.session['password'] = dict['PASSWORD']
                request.session['account_type'] = dict['ACCOUNT TYPE']
                request.session['login_message'] = "Login Successful! Welcome, "+dict['NAME']
                #request.session['cart_size'] = len(Get_Cart(dict['ID']))
                return redirect('/home/')
                # return HttpResponseRedirect(reverse('books:home'))
                # return render(request, 'books/home.html', dict)
            else:
                form = LoginForm()
                dict = {}
                dict['login_message'] = "Login Failed! Sorry"
                dict['form'] = form
                return render(request, 'books/index.html', dict)
    else:
        request.session.flush()
        form = LoginForm()
        return render(request , 'books/index.html' , {'form':form})

def CreateCustomer(id,username , email , mobile , address , password , account_type):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO "MYSELF"."USER"(ID , MOBILE , ADDRESS , EMAIL ,  NAME , PASSWORD , "ACCOUNT TYPE")
                    VALUES(:id,:mobile,:address,:email,:username,:password ,:account_type)
                    ''',[id, mobile, address, email, username , password , account_type])
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
            id = int(Max_CustomerID())
            id = id+1
            print("******")
            print(id)
            CreateCustomer(id, username, email, mobile, address , password , 'customer')

            all_customers = All_Users()
            dict = Get_Current_Customer(all_customers, username)
            request.session['username'] = dict['NAME']
            request.session['id'] = dict["ID"]
            request.session['mobile'] = dict['MOBILE']
            request.session['email'] = dict['EMAIL']
            request.session['address'] = dict['ADDRESS']
            request.session['password'] = dict['PASSWORD']
            request.session['account_type'] = dict['ACCOUNT TYPE']
            request.session['login_message'] ="Congratulations "+dict['NAME'] +", Sign Up Successful"
            return redirect('/home/')
    else:
        form = UserForm()
    return render(request, 'books/signup.html', {'form': form})


def Update_Customer(id,username, email, mobile, address, password):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    cursor.execute(
        '''delete from "MYSELF"."USER" where ID=:id'''
        ,[id]
    )
    conn.commit()
    conn.close()
    CreateCustomer(id,username,email,mobile,address,password,'Customer')
    print('updateddd')


def user_profile(request):
    if request.method == "POST":
        form = User_Profile_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            id = request.session.get('id')  #"getting current customer's id"

            Update_Customer(id, username, email, mobile, address, password)
            all_customers = All_Users()
            dict = Get_Current_Customer(all_customers, username)
            request.session['username'] = dict['NAME']
            request.session['id'] = dict["ID"]
            request.session['mobile'] = dict['MOBILE']
            request.session['email'] = dict['EMAIL']
            request.session['address'] = dict['ADDRESS']
            request.session['password'] = dict['PASSWORD']
            request.session['account_type'] = dict['ACCOUNT TYPE']

            form = User_Profile_Form()
            form.fields['username'].initial = dict['NAME']
            form.fields['password'].initial = '*'*len(dict['PASSWORD'])
            form.fields['email'].initial = dict['EMAIL']
            form.fields['mobile'].initial = dict['MOBILE']
            form.fields['account_type'].initial = dict['ACCOUNT TYPE']
            form.fields['address'].initial = dict['ADDRESS']

            s={}
            s['username'] = dict['NAME']
            s['mobile'] = dict['MOBILE']
            s['email'] = dict['EMAIL']
            s['address'] = dict['ADDRESS']
            s['account_type'] = dict['ACCOUNT TYPE']
            s['password'] = dict['PASSWORD']
            s['form'] = form
            s['cart_size'] = len(Get_Cart(request.session.get('id')))
            return render(request, 'books/user_profile.html', s)
    elif request.session.has_key('username'):
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        form = User_Profile_Form()
        form.fields['username'].initial=dict['username']
        form.fields['password'].initial = dict['password']
        form.fields['email'].initial = dict['email']
        form.fields['mobile'].initial = dict['mobile']
        form.fields['account_type'].initial = dict['account_type']
        form.fields['address'].initial = dict['address']
        dict['form'] = form
        print(form)
        return render(request , 'books/user_profile.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'books/index.html' , {'form':form})


def home(request):
    if request.session.has_key('username'):
        dict={}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['login_message'] = request.session.get('login_message')
        dict['cart_size'] = len(Get_Cart(request.session.get('id')))
        return render(request, 'books/home.html', dict)
    else:
        #print("home session not found")
        form = LoginForm()
        return render(request, 'books/index.html' , {'form':form})
        # # return index(request)

def order(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    customer_id = request.session.get('id')
    res = Get_Cart(customer_id)
    print(Max_OrderID())
    order_id = int(Max_OrderID()) + 1
    print("order_id :" + str(order_id))
    status = 'Pending'
    cursor.execute('''
                        INSERT INTO "MYSELF"."ORDER_HISTORY"("ORDER_ID" , "CUSTOMER_ID", "STATUS")
                        VALUES(:order_id,:customer_id,:status)
                        ''', [order_id, customer_id, status])
    for item in res:
        quantity = request.GET.get(item['ID'])
        book_id = item['ID']
        cursor.execute('''
                            UPDATE "MYSELF"."CART"
                            SET "QUANTITY" = :quantity, "ORDER_ID" = :order_id 
                            WHERE "ID" = :book_id AND "CUSTOMER ID" = :customer_id AND "QUANTITY" =:q AND "ORDER_ID" =:o
                            ''',
                       {'quantity': int(quantity),
                        'order_id': order_id,
                        'book_id': int(book_id),
                        'customer_id': int(customer_id),
                        'q': -1,
                        'o': -1,
                        })

    conn.commit()
    conn.close()
    return redirect( 'books:specificOrder', order_id=order_id)

def specificOrder( request, order_id):
    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['order_id'] = order_id
    dict['cart_size'] = len(Get_Cart(request.session.get('id')))
    res = Get_Cart( dict['id'], order_id)
    print(res)
    lst = []
    for item in res:
        a, b, c = Get_Book_Name_Price(item['ID'])
        lst.append((a, b, c, item['QUANTITY']))
    dict['specificOrder'] = lst
    print(dict['specificOrder'])
    total = 0
    for a, b, c, d in dict['specificOrder']:
        total += int(c) * int(d)
    dict['total'] = total
    dict['status'] = GET_ORDER_STATUS(order_id)
    return render(request, 'books/specificOrder.html', dict)

def allOrder( request):
    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = len(Get_Cart(request.session.get('id')))
    res = Get_Order_IDs(dict['id'])
    lst = []
    for item in res:
        lst.append(item['ORDER_ID'])
    lst.sort(reverse=True)
    f_list = []
    for it in lst:
        res = Get_Cart( dict['id'], it)
        lt = []
        p = {}
        for item in res:
            a, b, c = Get_Book_Name_Price(item['ID'])
            lt.append((a, b, c, item['QUANTITY']))
        total = 0
        for a, b, c, d in lt:
            total += int(c)
        p['total'] = total
        p['lst'] = lt
        p['status'] = GET_ORDER_STATUS(it)
        p['order_id'] = it
        f_list.append(p)
    dict['allOrderItems'] = f_list
    return render( request, 'books/allOrders.html', dict)

def bookDetails( request, book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."BOOK"
                            WHERE "BOOK ID" =: book_id''',
                   {'book_id' : book_id})
    res = dictfetchall(cursor)
    conn.close()
    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = len(Get_Cart(request.session.get('id')))
    book = {}
    book['isbn'] = res[0]['ISBN']
    book['title'] = res[0]['TITLE']
    book['edition'] = res[0]['EDITION']
    book['pages'] = res[0]['NO OF PAGES']
    book['language'] = res[0]['LANGUAGE']
    book['price'] = res[0]['PRICE']
    book['author'] = Get_Author_Name(res[0]['AUTHOR ID'])
    book['publisher'] = Get_Publisher_Name(res[0]['PUBLISHER ID'])
    book['category'] = Get_Category_Name(res[0]['CATEGORY ID'])
    book['id'] = book_id
    book['averageRating'] = getAverageRating(book_id)
    book['userRating'] = getCustomerRating(dict['id'], book_id)
    print(book['averageRating'])
    print(book['userRating'])
    book['comments'] = getComment(book_id)
    book['image'] = res[0]['IMAGE_SRC']
    print(book['image'])
    dict['theBook'] = book
    return render( request, 'books/bookDetails.html', dict)

def addToCart( request, book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    quantity = -1
    order_id = -1
    customer_id = request.session.get('id')
    cursor.execute('''delete from "MYSELF"."CART" where "ID" =:book_id and "CUSTOMER ID" =:customer_id
                            ''', {'book_id': book_id, 'customer_id': customer_id})
    cursor.execute('''
                    INSERT INTO "MYSELF"."CART"("ID", "CUSTOMER ID", "QUANTITY", "ORDER_ID")
                    VALUES(:book_id, :customer_id, :quantity, :order_id)
                    ''', [book_id, customer_id, quantity, order_id])
    conn.commit()
    conn.close()
    return redirect('books:bookDetails', book_id = book_id)

def giveRating( request, book_id):
    id = int(Max_OrderID()) + 1
    stars = request.GET.get(book_id)
    print(stars)
    electronic_id = -1
    customer_id = request.session.get('id')
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM "MYSELF"."RATING"
                               WHERE "BOOK ID" =: book_id AND "CUSTOMER ID" =: customer_id''',
                   {'book_id': book_id, 'customer_id': customer_id})
    cursor.execute('''
                        INSERT INTO "MYSELF"."RATING"("ID", "STARS", "BOOK ID", "ELECTRONIC ID", "CUSTOMER ID")
                        VALUES(:id, :stars, :book_id, :electronic_id, :customer_id)
                        ''', [ id, stars, book_id, electronic_id, customer_id])
    conn.commit()
    conn.close()
    return redirect('books:bookDetails', book_id = book_id)


def addComment( request, book_id):
    id = int(Max_Comment()) + 1
    pcomment = request.GET.get(book_id)
    print(pcomment)
    electronic_id = -1
    customer_id = request.session.get('id')
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    INSERT INTO "MYSELF"."COMMENT"("ID", "DESCRIPTION", "BOOK ID", "ELECTRONIC ID", "CUSTOMER ID")
                    VALUES( :id, :pcomment, :book_id, :electronic_id, :customer_id)
                    ''', [id, pcomment, book_id, electronic_id, customer_id])
    conn.commit()
    conn.close()
    return redirect('books:bookDetails', book_id = book_id)