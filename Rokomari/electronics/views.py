from django.shortcuts import render
from home.forms import *
from miscellaneous.miscellaneous import *
import cx_Oracle


def electronics_category(request):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        dict={}
        cursor.execute( '''SELECT * FROM MYSELF."ELECTRONICS CATEGORY"''')
        res = dict_fetch_all(cursor)
        conn.close()
        ctg_id = [x['ID'] for x in res]
        ctg_name = [x['NAME'] for x in res]
        dict['category'] = [(x[0], x[1]) for x in zip(ctg_id, ctg_name)]
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
        return render(request, 'electronics/electronics_category.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def electronics_category_details(request, ctg_id):
    if 'username' in request.session:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        #complex query can be done here
        cursor.execute(
            '''SELECT * FROM "MYSELF"."ELECTRONICS" where "CATEGORY ID" = :ctg_id
            ''', [ctg_id]
        )
        res = dict_fetch_all(cursor)
        conn.close()
        for electronics in res:
            electronics['BRAND_NAME'] = get_brand_name(electronics['BRAND ID'])
        dict = {'electronics': res, 'category_name': get_electronics_category_name(ctg_id), 'category_id': ctg_id,
                'username': request.session.get('username'), 'id': request.session.get('id'),
                'mobile': request.session.get('mobile'), 'email': request.session.get('email'),
                'address': request.session.get('address'), 'account_type': request.session.get('account_type'),
                'password': request.session.get('password'), 'cart_size': len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id'))),
                'wishlist_size':len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))}
        return render(request, 'electronics/electronics_category_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def electronics_brand(request):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM "MYSELF"."BRAND"''')
        res = dict_fetch_all(cursor)
        conn.close()
        brand_id = [x['ID'] for x in res]
        brand_name = [x['NAME'] for x in res]
        dict= {'brand': [(x[0], x[1]) for x in zip(brand_id, brand_name)], 'username': request.session.get('username'),
               'id': request.session.get('id'), 'mobile': request.session.get('mobile'),
               'email': request.session.get('email'), 'address': request.session.get('address'),
               'account_type': request.session.get('account_type'), 'password': request.session.get('password'),
               'cart_size': len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id'))),
               'wishlist_size' : len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))}
        return render(request, 'electronics/electronics_brand.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def electronics_brand_details(request, brand_id, electronics_id=None):
    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute(
            '''SELECT * FROM "MYSELF"."ELECTRONICS" WHERE "BRAND ID"=:brand_id
            ''', [brand_id]
        )
        res = dict_fetch_all(cursor)
        conn.close()
        for electronics in res:
            electronics['CATEGORY_NAME'] = get_electronics_category_name(electronics['CATEGORY ID'])
        dict = {'electronics': res, 'brand_name': get_brand_name(brand_id), 'username': request.session.get('username'),
                'id': request.session.get('id'), 'mobile': request.session.get('mobile'),
                'email': request.session.get('email'), 'address': request.session.get('address'),
                'account_type': request.session.get('account_type'), 'password': request.session.get('password'),
                'brand_id': brand_id, 'cart_size': len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id'))),
                'wishlist_size':len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))}
        return render(request, 'electronics/electronics_brand_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def electronics_details(request, electronics_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."ELECTRONICS" WHERE "ID" =: electronics_id''',
                   {'electronics_id' : electronics_id})
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
    dict['wishlist_size'] = len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))
    electronics = {}
    electronics['title'] = res[0]['TITLE']
    electronics['price'] = res[0]['PRICE']
    electronics['model'] = res[0]['MODEL']
    electronics['brand'] = get_brand_name(res[0]['BRAND ID'])
    electronics['category'] = get_electronics_category_name(res[0]['CATEGORY ID'])
    electronics['id'] = electronics_id
    electronics['description'] = res[0]['DESCRIPTION']
    electronics['warranty'] = res[0]['WARRANTY']

    electronics['stock'] = res[0]['STOCK']
    electronics['averageRating'] = get_average_rating(electronics_id)
    electronics['userRating'] = get_customer_rating(dict['id'], electronics_id)
    #print(res[0]['WARRANTY'])
    #print(electronics['userRating'])

    electronics['comments'] = get_comment(electronics_id)
    electronics['image'] = res[0]['IMAGE_SRC']
    print(electronics['image'])
    dict['theElectronics'] = electronics
    return render(request, 'electronics/electronics_details.html', dict)
