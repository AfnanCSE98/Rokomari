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
        cursor.execute('''SELECT * FROM MYSELF."BOOK CATEGORY"''')
        res = dict_fetch_all(cursor)
        conn.close()


        ctg_ID = [x['ID'] for x in res]
        ctg_NAME = [x['NAME'] for x in res]


        dict = {}
        dict['category'] = [(x[0], x[1]) for x in zip(ctg_ID, ctg_NAME)]
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['none'] = None
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        return render(request , 'books/book_category.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_category_details(request, ctg_id):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT ID, TITLE, 
                            (SELECT "NAME" FROM MYSELF.AUTHOR A WHERE A.ID = B."AUTHOR ID") AUTHOR_NAME,
                            (SELECT "NAME" FROM MYSELF.PUBLISHER P WHERE P.ID = B."PUBLISHER ID") PUBLISHER_NAME,
                                PRICE FROM MYSELF.BOOK B WHERE "CATEGORY ID" =: ctg_id
            ''', [ctg_id])
        res = dict_fetch_all(cursor)
        conn.close()


        dict = {}
        dict['book'] = res
        dict['category_name'] = get_book_category_name(ctg_id)
        dict['category_id'] = ctg_id
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len( dict['id'], 1) + get_electronics_cart_len( dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len( dict['id']) + get_electronics_wishlist_len(dict['id'])

        return render(request, 'books/book_category_details.html', dict)
    else:
        form = LoginForm()

        return render(request, 'home/index.html', {'form': form})


def book_author(request):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM MYSELF.AUTHOR ''')
        res = dict_fetch_all(cursor)
        conn.close()


        author_id = [x['ID'] for x in res]
        author_name = [x['NAME'] for x in res]


        dict = {}
        dict['author'] = [(x[0], x[1]) for x in zip(author_id, author_name)]
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

        return render(request, 'books/book_author.html', dict)
    else:
        form = LoginForm()

        return render(request, 'home/index.html', {'form': form})


def book_author_details(request, author_id):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT ID, TITLE, (SELECT "NAME" FROM MYSELF."BOOK CATEGORY" C WHERE C.ID = B."CATEGORY ID") CATEGORY_NAME,
                                    (SELECT "NAME" FROM MYSELF.PUBLISHER P WHERE P.ID = B."PUBLISHER ID") PUBLISHER_NAME,
                                        PRICE FROM MYSELF.BOOK B WHERE "AUTHOR ID" = :author_id
                    ''', [author_id])
        res = dict_fetch_all(cursor)
        conn.close()


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
        dict['cart_size'] = get_book_cart_len( dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

        return render(request, 'books/book_author_details.html', dict)
    else:
        form = LoginForm()

        return render(request, 'home/index.html', {'form': form})


def book_publisher(request):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM MYSELF.PUBLISHER''')
        res = dict_fetch_all(cursor)
        conn.close()


        pub_id = [x['ID'] for x in res]
        pub_name = [x['NAME'] for x in res]


        dict={}
        dict['publisher'] = [(x[0], x[1]) for x in zip(pub_id, pub_name)]
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

        return render(request , 'books/book_publisher.html' , dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def book_publisher_details(request, pub_id):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT ID, TITLE, (SELECT "NAME" FROM MYSELF."BOOK CATEGORY" C WHERE C.ID = B."CATEGORY ID") CATEGORY_NAME,
                                            (SELECT "NAME" FROM MYSELF.AUTHOR A WHERE A.ID = B."AUTHOR ID") AUTHOR_NAME,
                                                PRICE FROM MYSELF.BOOK B WHERE "PUBLISHER ID" = :pub_id
                            ''', [pub_id]
                       )
        res = dict_fetch_all(cursor)
        conn.close()


        dict = {}
        dict['book'] = res
        dict['publisher_name'] = get_publisher_name(pub_id)
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['publisher_id'] = pub_id
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

        return render(request, 'books/book_publisher_details.html', dict)
    else:
        form = LoginForm()

        return render(request, 'home/index.html', {'form': form})


def book_details(request, book_id):

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    customer_id = request.session.get('id')
    cursor.execute('''SELECT ISBN, TITLE, EDITION, "NO OF PAGES", LANGUAGE, PRICE, 
                        (SELECT NAME FROM AUTHOR A WHERE A.ID = B."AUTHOR ID") "AUTHOR NAME", 
                        (SELECT  NAME FROM PUBLISHER P WHERE P.ID = B."PUBLISHER ID") "PUBLISHER NAME",
                        (SELECT  NAME FROM "BOOK CATEGORY" C WHERE C.ID = B."CATEGORY ID") "CATEGORY NAME",
                        (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."BOOK ID" = B.ID) "AVERAGE RATING",
                        (SELECT TO_NUMBER(STARS) FROM RATING R WHERE R."BOOK ID" = B.ID AND "USER ID" =: customer_id) "USER RATING",
                        IMAGE_SRC FROM BOOK B WHERE "ID" =: book_id
                        ''', [customer_id, book_id])
    res = dict_fetch_all(cursor)
    conn.close()


    book = {}
    book['isbn'] = res[0]['ISBN']
    book['title'] = res[0]['TITLE']
    book['edition'] = res[0]['EDITION']
    book['pages'] = res[0]['NO OF PAGES']
    book['language'] = res[0]['LANGUAGE']
    book['price'] = res[0]['PRICE']
    book['author'] = res[0]['AUTHOR NAME']
    book['publisher'] = res[0]['PUBLISHER NAME']
    book['category'] = res[0]['CATEGORY NAME']
    book['id'] = book_id
    book['averageRating'] = res[0]['AVERAGE RATING']
    book['userRating'] = get_customer_rating(customer_id, book_id)
    book['comments'] = get_comment(book_id)
    book['image'] = res[0]['IMAGE_SRC']


    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len( dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
    dict['theBook'] = book

    return render(request, 'books/book_details.html', dict)
