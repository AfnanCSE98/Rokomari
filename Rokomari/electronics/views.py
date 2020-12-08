from django.shortcuts import render
from home.forms import *
from miscellaneous.miscellaneous import *
import cx_Oracle


def electronics_category(request):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute( '''SELECT * FROM MYSELF."ELECTRONICS CATEGORY"''')
        res = dict_fetch_all(cursor)
        conn.close()


        ctg_id = [x['ID'] for x in res]
        ctg_name = [x['NAME'] for x in res]


        dict = {}
        dict['category'] = [(x[0], x[1]) for x in zip(ctg_id, ctg_name)]
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

        return render(request, 'electronics/electronics_category.html', dict)
    else:
        form = LoginForm()

        return render(request, 'home/index.html', {'form': form})


def electronics_category_details(request, ctg_id):

    if 'username' in request.session:
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT ID, TITLE, PRICE,  
                            (SELECT B.NAME FROM MYSELF.BRAND B WHERE B.ID = E."BRAND ID") BRAND_NAME,
                            (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID) "AVERAGE RATING",
                            IMAGE_SRC FROM MYSELF.ELECTRONICS E WHERE "CATEGORY ID" = :ctg_id
                        ''', [ctg_id])
        res = dict_fetch_all(cursor)
        conn.close()

        for item in res:
            if not isinstance(item['AVERAGE RATING'], type(None)):
                item['star_list'] = get_star_list(int(item['AVERAGE RATING']))


        dict = {}
        dict['electronics'] = res
        dict['category_name'] = get_electronics_category_name(ctg_id)
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])


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


        dict = {}
        dict['brand'] = [(x[0], x[1]) for x in zip(brand_id, brand_name)]
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len( dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

        return render(request, 'electronics/electronics_brand.html', dict)
    else:
        form = LoginForm()

        return render(request, 'home/index.html', {'form': form})


def electronics_brand_details(request, brand_id):

    if request.session.has_key('username'):
        dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
        conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
        cursor = conn.cursor()
        cursor.execute('''SELECT ID, TITLE, PRICE,
                            (SELECT C.NAME FROM MYSELF."ELECTRONICS CATEGORY" C WHERE C.ID = E."CATEGORY ID") CATEGORY_NAME,
                            (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID) "AVERAGE RATING",
                            IMAGE_SRC FROM MYSELF.ELECTRONICS E WHERE "BRAND ID"=:brand_id''', [brand_id])
        res = dict_fetch_all(cursor)
        conn.close()

        for item in res:
            if not isinstance(item['AVERAGE RATING'], type(None)):
                item['star_list'] = get_star_list(int(item['AVERAGE RATING']))

        dict = {}
        dict['electronics'] = res
        dict['brand_name'] = get_brand_name(brand_id)
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])


        return render(request, 'electronics/electronics_brand_details.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})


def electronics_details(request, electronics_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    customer_id = request.session.get('id')
    cursor.execute('''SELECT TITLE, PRICE, DESCRIPTION, WARRANTY, MODEL, STOCK, DESCRIPTION, 
                            (SELECT  NAME FROM BRAND B WHERE B.ID = E."BRAND ID") "BRAND NAME",
                            (SELECT  NAME FROM "ELECTRONICS CATEGORY" C WHERE C.ID = E."CATEGORY ID") "CATEGORY NAME",
                            GET_AVERAGE_ELECTRONICS_RATING(ID) "AVERAGE RATING",
                            (SELECT TO_NUMBER(STARS) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID AND "USER ID" =: customer_id) "USER RATING",
                            IMAGE_SRC FROM ELECTRONICS E WHERE "ID" =: book_id
                            ''', [customer_id, electronics_id])
    res = dict_fetch_all(cursor)
    conn.close()
    """
    (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID)
    """
    electronics = {}
    electronics['title'] = res[0]['TITLE']
    electronics['price'] = res[0]['PRICE']
    electronics['brand'] = res[0]['BRAND NAME']
    electronics['category'] = res[0]['CATEGORY NAME']
    electronics['id'] = electronics_id
    electronics['description'] = res[0]['DESCRIPTION']
    electronics['warranty'] = res[0]['WARRANTY']
    electronics['averageRating'] = res[0]['AVERAGE RATING']
    electronics['userRating'] = res[0]['USER RATING']
    electronics['comments'] = get_comment(electronics_id)
    electronics['image'] = res[0]['IMAGE_SRC']
    electronics['model'] = res[0]['MODEL']
    electronics['stock'] = int(res[0]['STOCK'])
    electronics['description'] = res[0]['DESCRIPTION']
    if not isinstance(electronics['averageRating'], type(None)):
        electronics['star_list'] = get_star_list(int(electronics['averageRating']))
    if not isinstance(electronics['userRating'], type(None)):
        electronics['star_list_user'] = get_star_list(int(electronics['userRating']))

    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
    dict['theElectronics'] = electronics


    return render(request, 'electronics/electronics_details.html', dict)
