from django.shortcuts import render
from miscellaneous.miscellaneous import *
from home.forms import *
import cx_Oracle

# Create your views here.

def book_category(request):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        dict={}
        cursor.execute(
            '''select * from MYSELF."BOOK CATEGORY"'''
        )
        res = dict_fetch_all(cursor)
        conn.close()
        ctg_ID=[x['ID'] for x in res]
        ctg_NAME=[x['NAME'] for x in res]
        dict['category'] = [(x[0], x[1]) for x in zip(ctg_ID, ctg_NAME)]
        "storing current customer information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['none'] = None
        dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id')))
        dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))
        return render(request , 'books/book_category.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_category_details(request, ctg_id):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.BOOK where "CATEGORY ID" = :ctg_id
            ''', [ctg_id]
        )
        res = dict_fetch_all(cursor)
        conn.close()
        for book in res:
            book['AUTHOR_NAME'] = get_author_name(book['AUTHOR ID'])
            book['PUBLISHER_NAME'] = get_publisher_name(book['PUBLISHER ID'])
        dict = {}
        dict['book'] = res
        dict['category_name'] = get_book_category_name(ctg_id)
        dict['category_id'] = ctg_id
        "Storing current customer information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id')))
        dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))
        return render(request, 'books/book_category_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_author(request):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.AUTHOR 
            '''
          )
        res = dict_fetch_all(cursor)
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
        dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(
            get_electronics_cart(request.session.get('id')))
        dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(
            get_electronics_wishlist(request.session.get('id')))
        return render(request, 'books/book_author.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_author_details(request, author_id):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.BOOK where "AUTHOR ID"=:author_id
            ''', [author_id]
        )
        res = dict_fetch_all(cursor)
        conn.close()
        for book in res:
            #book['ID'] = book['BOOK ID']
            book['PUBLISHER_NAME'] = get_publisher_name(book['PUBLISHER ID'])
            book['CATEGORY_NAME'] = get_book_category_name(book['CATEGORY ID'])
        dict = {}
        dict['book'] = res
        dict['author_name'] = get_author_name(author_id)
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['author_id'] = author_id

        dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(
            get_electronics_cart(request.session.get('id')))
        dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(
            get_electronics_wishlist(request.session.get('id')))
        return render(request, 'books/book_author_details.html', dict)

    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_publisher(request):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.PUBLISHER
            '''
        )
        res = dict_fetch_all(cursor)
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
        dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id')))
        dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(
            get_electronics_wishlist(request.session.get('id')))
        return render(request , 'books/book_publisher.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_publisher_details(request, pub_id):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''select * from MYSELF.BOOK where "PUBLISHER ID"=:pub_id
            ''', [pub_id]
        )
        res = dict_fetch_all(cursor)
        conn.close()
        for book in res:
            #book['ID'] = book['BOOK ID']
            book['AUTHOR_NAME'] = get_author_name(book['AUTHOR ID'])
            book['CATEGORY_NAME'] = get_book_category_name(book['CATEGORY ID'])
        dict = {}
        dict['book'] = res
        dict['publisher_name'] = get_publisher_name(pub_id)
        "Storing current user information"
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['publisher_id'] = pub_id
        dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id')))
        dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(
            get_electronics_wishlist(request.session.get('id')))
        return render(request, 'books/book_publisher_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_details(request, book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."BOOK"
                            WHERE "ID" =: book_id''',
                   {'book_id' : book_id})
    res = dict_fetch_all(cursor)
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
    dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id')))
    dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(
        get_electronics_wishlist(request.session.get('id')))
    book = {}
    book['isbn'] = res[0]['ISBN']
    book['title'] = res[0]['TITLE']
    book['edition'] = res[0]['EDITION']
    book['pages'] = res[0]['NO OF PAGES']
    book['language'] = res[0]['LANGUAGE']
    book['price'] = res[0]['PRICE']
    book['author'] = get_author_name(res[0]['AUTHOR ID'])
    book['publisher'] = get_publisher_name(res[0]['PUBLISHER ID'])
    book['category'] = get_book_category_name(res[0]['CATEGORY ID'])
    book['id'] = book_id
    book['averageRating'] = get_average_rating(book_id)
    book['userRating'] = get_customer_rating(dict['id'], book_id)
    print(book['averageRating'])
    print(book['userRating'])
    book['comments'] = get_comment(book_id)
    book['image'] = res[0]['IMAGE_SRC']
    print(book['image'])
    dict['theBook'] = book
    return render(request, 'books/book_details.html', dict)
