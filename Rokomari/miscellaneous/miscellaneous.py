import cx_Oracle
import hashlib
import os
import binascii
THRESHOLD = int(1e6)
star_list = ['', '*', '**', '***', '****', '*****']

def dict_fetch_all(cursor):
    """
    Return all rows from a cursor as a dict
    """
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def max_customer_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."USER" ''')
    res = cursor.fetchall()
    print(res)
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]


def max_order_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."ORDER HISTORY" ''')
    res = cursor.fetchall()
    print(res)
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]


def max_rating_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."RATING" ''')
    res = cursor.fetchall()
    print(res[0][0])
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]


def max_comment_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."COMMENT" ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]


def max_wishlist_id(product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."BOOK WISHLIST" ''')
    else:
        cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."ELECTRONICS WISHLIST" ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]


def max_cart_id(product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."BOOK CART" ''')
    else:
        cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "MYSELF"."ELECTRONICS CART" ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]


def get_book_wishlist(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT W."BOOK ID", B."TITLE", B."PRICE"
                            FROM "MYSELF"."BOOK WISHLIST" W JOIN "MYSELF"."BOOK" B
                            ON (W."BOOK ID" = B.ID )
                            WHERE W."USER ID" =:customer_id
                                ''', [customer_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res


def get_book_wishlist_len(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NVL(COUNT("ID"), 0) BWL FROM MYSELF."BOOK WISHLIST"
                                WHERE "USER ID" =:customer_id''', [customer_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['BWL'])

def get_electronics_wishlist(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT W."ELECTRONICS ID", E."TITLE", E."PRICE"
                                FROM "MYSELF"."ELECTRONICS WISHLIST" W JOIN "MYSELF"."ELECTRONICS" E
                                ON (W."ELECTRONICS ID" = E.ID )
                                WHERE W."USER ID" =:customer_id
                                    ''', [customer_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res

def get_electronics_wishlist_len(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NVL(COUNT("ID"), 0) EWL FROM MYSELF."ELECTRONICS WISHLIST"
                                WHERE "USER ID" =:customer_id''', [customer_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['EWL'])

def get_book_cart(customer_id, order_id = 1):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT C."BOOK ID", C."BOOK QUANTITY", B."TITLE", B."PRICE"
                        FROM "MYSELF"."BOOK CART" C JOIN "MYSELF"."BOOK" B
                        ON (C."BOOK ID" = B.ID )
                        WHERE C."USER ID" =:customer_id AND C."ORDER ID" =:order_id
                            ''', [customer_id, order_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res

def get_book_cart_len( customer_id, order_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NVL(COUNT("ID"), 0) BCL FROM MYSELF."BOOK CART"
                                WHERE "USER ID" =:customer_id AND "ORDER ID" =: order_id''', [customer_id, order_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['BCL'])


def get_electronics_cart(customer_id, order_id = 1):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT C."ELECTRONICS ID", C."ELECTRONICS QUANTITY", E."TITLE", E."PRICE"
                            FROM "MYSELF"."ELECTRONICS CART" C JOIN "MYSELF"."ELECTRONICS" E
                            ON (C."ELECTRONICS ID" = E.ID )
                            WHERE C."USER ID" =:customer_id AND C."ORDER ID" =:order_id
                                ''', [customer_id, order_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res

def get_electronics_cart_len(customer_id, order_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NVL(COUNT("ID"), 0) ECL FROM MYSELF."ELECTRONICS CART"
                                WHERE "USER ID" =:customer_id AND "ORDER ID" =: order_id''', [customer_id, order_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['ECL'])


def get_product_name_price(product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT TITLE, PRICE FROM "MYSELF"."BOOK" WHERE "ID"=:product_id
                    ''', [product_id]
        )
    else:
        cursor.execute('''SELECT TITLE, PRICE FROM "MYSELF"."ELECTRONICS" WHERE "ID"=:product_id
                            ''', [product_id]
                       )
    res = dict_fetch_all(cursor)
    conn.close()
    return product_id, res[0]['TITLE'], res[0]['PRICE']

def get_product_quantity(user_id, product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT "BOOK QUANTITY" FROM "MYSELF"."BOOKS" WHERE "ID"=:product_id AND 
                    ''', [product_id]
        )
    else:
        cursor.execute('''SELECT "ELECTRONICS QUANTITY" FROM "MYSELF"."ELECTRONICS" WHERE "ID"=:product_id
                            ''', [product_id]
                       )
    res = dict_fetch_all(cursor)
    conn.close()
    return product_id, res[0]['TITLE'], res[0]['PRICE']


def get_order_status(order_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT STATUS FROM "MYSELF"."ORDER HISTORY" WHERE ID=:order_id
                    ''', [order_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res[0]['STATUS']


def get_brand_name(brand_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM "MYSELF"."BRAND" where ID=:brand_id
                    ''', [brand_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res[0]['NAME']


def get_electronics_category_name(ctg_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM "MYSELF"."ELECTRONICS CATEGORY" WHERE ID=:ctg_id
                    ''', [ctg_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res[0]['NAME']

def get_book_category_name(ctg_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM "MYSELF"."BOOK CATEGORY" WHERE ID=:ctg_id
                    ''', [ctg_id])
    res = dict_fetch_all(cursor)
    conn.close()
    return res[0]['NAME']

def get_order_ids(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT oh.ID, oh."ORDER TIME" FROM "MYSELF"."ORDER HISTORY" oh WHERE "USER ID" =:customer_id
                        ''', [customer_id])

    res = dict_fetch_all(cursor)
    conn.close()
    return res


def get_customer_name(customer_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT NAME FROM "MYSELF"."USER"
                        WHERE ID =: customer_id''', {'customer_id': customer_id})
    res = dict_fetch_all(cursor)
    conn.close()
    if len(res):
        return res[0]['NAME']
    else:
        return None


def get_customer_rating(customer_id, product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT STARS FROM "MYSELF"."RATING"
                    WHERE "USER ID" =: customer_id AND "BOOK ID" =: product_id''',
                   {'customer_id': customer_id, 'product_id': product_id})
    else:
        cursor.execute('''SELECT STARS FROM "MYSELF"."RATING"
                            WHERE "USER ID" =: customer_id AND "ELECTRONICS ID" =: product_id''',
                       {'customer_id': customer_id, 'product_id': product_id})
    res = dict_fetch_all(cursor)
    conn.close()
    if len(res):
        return res[0]['STARS']
    else:
        return None


def get_average_rating(product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    #complex query can be written here
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT STARS FROM "MYSELF"."RATING"
                    WHERE "BOOK ID" =: product_id''',
                       {'product_id': product_id})
    else:
        cursor.execute('''SELECT STARS FROM "MYSELF"."RATING"
                            WHERE "ELECTRONICS ID" =: product_id''',
                       {'product_id': product_id})
    res = dict_fetch_all(cursor)
    conn.close()
    sum = 0
    len = 0
    for item in res:
        sum += int(item['STARS'])
        len += 1
    if sum == 0:
        return None
    else:
        return round(sum/len, 0)


def get_comment(product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    #complex query can written here
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT ID, DESCRIPTION, "USER ID" FROM "MYSELF"."COMMENT"
                    WHERE "BOOK ID" =: product_id''',
                       {'product_id': product_id})
    else:
        cursor.execute('''SELECT ID, DESCRIPTION, "USER ID" FROM "MYSELF"."COMMENT"
                            WHERE "ELECTRONICS ID" =: product_id''',
                       {'product_id': product_id})
    res = dict_fetch_all(cursor)
    conn.close()
    lst = []
    if int(product_id) < THRESHOLD:
        for item in res:
            lst.append((int(item['ID']), item['DESCRIPTION'], get_customer_name(item['USER ID'])))
            print(item['USER ID'])
    else:
        for item in res:
            lst.append((int(item['ID']), item['DESCRIPTION'], get_customer_name(item['USER ID'])))
            print(item['USER ID'])
    lst.sort(reverse=True)
    return lst


def get_author_name(author_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select NAME from MYSELF.AUTHOR where ID=:author_id
        ''', [author_id]
    )
    res = dict_fetch_all(cursor)
    conn.close()
    return res[0]['NAME']


def get_publisher_name(publisher_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select NAME from MYSELF.PUBLISHER where ID =: publisher_id
        ''',[publisher_id]
    )
    res = dict_fetch_all(cursor)
    conn.close()
    return res[0]['NAME']

def authenticate(username, password):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."USER" WHERE NAME=:username''', [username])
    row = dict_fetch_all(cursor)
    conn.close()
    print(row)
    for user in row:
        salt = binascii.a2b_hex(user['SALT'])
        key = binascii.a2b_hex(user['KEY'])
        new_key = binascii.b2a_hex(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000))
        print(username)
        print(key)
        print(binascii.b2a_hex(new_key))
        if key == new_key:
            print('ok')
            return True
    return False

def check_username(username):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."USER" WHERE NAME=:username''', [username])
    row = dict_fetch_all(cursor)
    conn.close()
    for user in row:
        if user['NAME'] == username:
            return True
    return False

def check_email(email):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."USER" WHERE NAME=:email''', [email])
    row = dict_fetch_all(cursor)
    conn.close()
    for user in row:
        if user['EMAIL'] == email:
            return True
    return False
def all_users():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."USER" ''')
    customers = dict_fetch_all(cursor)
    conn.close()
    return customers


def get_current_customer(all_customer, username):
    """
    all_customer have all the customers.
    We return current customer from this list
    """
    for user in all_customer:
        print(user)
        if user['NAME'] == username:
            return user


def create_customer(id, username, email, mobile, address, password, account_type):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    salt = os.urandom(32)
    salt = binascii.b2a_hex(salt)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    key = binascii.b2a_hex(key)
    cursor.execute('''
                    INSERT INTO "MYSELF"."USER"(ID , "PHONE NUMBER" , ADDRESS , EMAIL ,  "NAME" , SALT, "KEY", TYPES)
                    VALUES(:id,:mobile,:address,:email,:username, :salt, :key,:account_type)
                    ''', [id, mobile, address, email, username, salt, key, account_type])
    conn.commit()
    conn.close()


def update_customer(id, username, email, mobile, address, password):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()

    salt = os.urandom(32)
    salt = binascii.b2a_hex(salt)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    key = binascii.b2a_hex(key)
    cursor.execute('''UPDATE "MYSELF"."USER"
                        SET "NAME" =: username,
                        EMAIL =: email,
                        "PHONE NUMBER" =: mobile,
                        ADDRESS =: address,
                        SALT =: salt,
                        "KEY" =: key
                        WHERE ID =: id
                        ''', [ username, email, mobile, address, salt, key, id])
    conn.commit()
    conn.close()
    print('updated')

def bestseller():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT TITLE , IMAGE_SRC , PRICE , ID, 
                        (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."BOOK ID" = B.ID) "AVERAGE RATING"
                        FROM MYSELF.BOOK B 
                        ORDER BY "SALES COUNT" DESC 
                        FETCH FIRST 5 ROWS ONLY''')
    res1 = dict_fetch_all(cursor)
    for item in res1:
        if not isinstance(item['AVERAGE RATING'], type(None)):
            item['star_list'] = get_star_list(int(item['AVERAGE RATING']))
            item['type'] = 'book'
    cursor.execute('''SELECT TITLE , IMAGE_SRC , PRICE , ID, 
                            (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID) "AVERAGE RATING"
                            FROM MYSELF.ELECTRONICS E
                            ORDER BY "SALES COUNT" DESC 
                            FETCH FIRST 5 ROWS ONLY''')
    res2 = dict_fetch_all(cursor)
    for item in res2:
        if not isinstance(item['AVERAGE RATING'], type(None)):
            item['star_list'] = get_star_list(int(item['AVERAGE RATING']))
    conn.close()
    res = res1 + res2
    return res


def get_orders_of_this_user(userid):
    res = get_order_ids(userid)
    lst = []
    for item in res:
        lst.append((int(item['ID']) , str(item['ORDER TIME'])))
    #lst.sort(reverse=True)
    f_list = []
    for it,time in lst:
        res1 = get_book_cart(userid, it)
        res2 = get_electronics_cart(userid, it)
        lt = []
        p = {}
        for item in res1:
            a, b, c = get_product_name_price(item['BOOK ID'])
            lt.append((a, b, c, item['BOOK QUANTITY']))
        for item in res2:
            a, b, c = get_product_name_price(item['ELECTRONICS ID'])
            lt.append((a, b, c, item['ELECTRONICS QUANTITY']))
        total = 0
        for a, b, c, d in lt:
            total += int(c) * int(d)
        p['total_price'] = total
        p['product'] = lt
        p['status'] = get_order_status(it)
        p['order_id'] = it
        p['time'] = time[:11]
        f_list.append(p)
    return f_list


def get_star_list(stars):
    for star in star_list:
        if len(star) == stars:
            return star

def get_book_sales(book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT "SALES COUNT" FROM MYSELF.BOOK WHERE ID =: book_id''', [book_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['SALES COUNT'])

def get_book_stock(book_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT "STOCK" FROM MYSELF.BOOK WHERE ID =: book_id''', [book_id])
    res = dict_fetch_all(cursor)
    print(res)
    return int(res[0]['STOCK'])

def get_electronics_sales(electronics_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT "SALES COUNT" FROM MYSELF.ELECTRONICS WHERE ID =: electronics_id''', [electronics_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['SALES COUNT'])

def get_electronics_stock(electronics_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT "STOCK" FROM MYSELF.ELECTRONICS WHERE ID =: electronics_id''', [electronics_id])
    res = dict_fetch_all(cursor)
    return int(res[0]['STOCK'])


def recently_sold():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT TITLE , IMAGE_SRC , PRICE , DISTINCT(ID), 
                            (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."BOOK ID" = B.ID) "AVERAGE RATING"
                            FROM MYSELF.BOOK B 
                            JOIN MYSELF."BOOK CART" C
                            ON(B.ID = C."BOOK ID")
                            JOIN MYSELF."ORDER HISTORY" O
                            ON(C."ORDER ID" = O.ID)
                            ORDER BY O."ORDER TIME" ASC 
                            FETCH FIRST 5 ROWS ONLY''')
    res1 = dict_fetch_all(cursor)
    for item in res1:
        if not isinstance(item['AVERAGE RATING'], type(None)):
            item['star_list'] = get_star_list(int(item['AVERAGE RATING']))
    cursor.execute('''SELECT TITLE , IMAGE_SRC , PRICE , DISTINCT(ID), 
                                (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID) "AVERAGE RATING"
                                FROM MYSELF.ELECTRONICS E
                                JOIN MYSELF."ELECTRONICS CART" C
                                ON(E.ID = C."ELECTRONICS ID")
                                JOIN MYSELF."ORDER HISTORY" O
                                ON(C."ORDER ID" = O.ID)
                                ORDER BY O."ORDER TIME" ASC  
                                FETCH FIRST 5 ROWS ONLY''')
    res2 = dict_fetch_all(cursor)
    for item in res2:
        if not isinstance(item['AVERAGE RATING'], type(None)):
            item['star_list'] = get_star_list(int(item['AVERAGE RATING']))
    conn.close()
    res = res1 + res2
    return res