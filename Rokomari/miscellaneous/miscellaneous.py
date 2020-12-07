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


def max_electronics_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM ELECTRONICS ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]

def max_brand_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM BRAND ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]

def max_electronics_category_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "ELECTRONICS CATEGORY" ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]

def max_book_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM BOOK ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]

def max_author_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM AUTHOR ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]

def max_publisher_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM PUBLISHER ''')
    res = cursor.fetchall()
    conn.close()
    if isinstance(res[0][0], type(None)):
        return 0
    else:
        return res[0][0]

def max_book_category_id():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT MAX(TO_NUMBER(ID)) FROM "BOOK CATEGORY" ''')
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


def is_admin(username, password):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."USER" WHERE NAME=:username''', [username])
    row = dict_fetch_all(cursor)
    conn.close()
    #print(row)
    for user in row:
        salt = binascii.a2b_hex(user['SALT'])
        key = binascii.a2b_hex(user['KEY'])
        new_key = binascii.b2a_hex(hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000))
        print(username)
        print(key)
        print(binascii.b2a_hex(new_key))
        if key == new_key and row[0]['TYPES'] == 'A':
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


def get_all_orders():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''
        select ID from MYSELF."USER"
        '''
    )
    res = dict_fetch_all(cursor)
    conn.close()
    user_ids=[]
    #print(res)
    #print("as")
    for i in res:
        user_ids.append(i['ID'])
    #print(user_ids)
    orders=[]
    """orders list is to store all the orders"""
    for id in user_ids:
        ord_of_id  = get_orders_of_this_user(id)
        for ord in ord_of_id:
            orders.append(ord)
    print(orders[0])
    return orders


def update_order_status(order_id):
    st  ='Delivered'
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''
        update MYSELF."ORDER HISTORY"
        set STATUS = :st
        where ID = :order_id
        ''',[st , order_id]
    )
    conn.commit()
    conn.close()



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

def get_brand_id(brand_name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    print(brand_name)
    brand_name = brand_name.upper()
    cursor.execute('''
                    SELECT ID FROM BRAND WHERE UPPER(TRIM("NAME")) =: brand_name''', [brand_name])
    res = dict_fetch_all(cursor)
    return res[0]['ID']

def get_electronics_category_id(category_name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    category_name = category_name.upper()
    cursor.execute('''
                        SELECT ID FROM "ELECTRONICS CATEGORY" WHERE UPPER(TRIM("NAME")) =: category_name''', [category_name])
    res = dict_fetch_all(cursor)
    return res[0]['ID']


"""Admin page related"""
def adding_electronics( title, model, price, image_src, description, warranty, brand_id, category_id, number_of_items_added):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    t_title = title.upper()
    t_model = model.upper()
    cursor.execute('''
    SELECT * FROM ELECTRONICS WHERE UPPER(TRIM(TITLE)) =: t_title AND UPPER(TRIM(MODEL)) =: t_model AND "BRAND ID" =: brand_id''',
                   [t_title, t_model, brand_id])
    res = dict_fetch_all(cursor)
    if len(res) == 0:
        sales_count = 0
        id = max_electronics_id() + 1
        cursor.execute('''
        INSERT INTO ELECTRONICS VALUES ( :id, :title, :model, :price, :image_src, :descricption, :warranty, :brand_id, :category_id, :number_of_items_added, 
        :sales_count)''', [id, title, model, price, image_src, description, warranty, brand_id, category_id, number_of_items_added, sales_count])
        conn.commit()
    conn.close()

def updating_electronics( title, model, price, warranty, brand_id, number_of_items_added):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    t_title = title.upper()
    t_model = model.upper()
    cursor.execute('''
    SELECT * FROM ELECTRONICS WHERE UPPER(TRIM(TITLE)) =: t_title AND UPPER(TRIM(MODEL)) =: t_model AND "BRAND ID" =: brand_id''',
                   [t_title, t_model, brand_id])
    res = dict_fetch_all(cursor)
    print(len(res))
    if len(res) > 0:
        id = res[0]['ID']
        print(id)
        stock = int(res[0]['STOCK']) + int(number_of_items_added)
        cursor.execute('''
        UPDATE ELECTRONICS
        SET PRICE =: price, WARRANTY =: warranty, STOCK =: stock
        WHERE ID =: id''', [price, warranty, stock, id])
        conn.commit()
    conn.close()

def adding_brand( name, phone_number, web_url, email, address, image_src):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    t_name = name.upper()
    cursor.execute('''
        SELECT * FROM BRAND WHERE UPPER(TRIM("NAME")) =: t_name''',
                   [t_name])
    res = dict_fetch_all(cursor)
    if len(res) == 0:
        id = max_brand_id() + 1
        cursor.execute('''
            INSERT INTO BRAND VALUES ( :id, :name, :phone_number, :web_url, :email, :address, :image_src 
            )''', [ id, name, phone_number, web_url, email, address, image_src])
        conn.commit()
    conn.close()

def adding_electronics_category(name, description, image_src):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    t_name = name.upper()
    cursor.execute('''
            SELECT * FROM "ELECTRONICS CATEGORY" WHERE UPPER(TRIM("NAME")) =: t_name''',
                   [t_name])
    res = dict_fetch_all(cursor)
    if len(res) == 0:
        id = max_electronics_category_id() + 1
        cursor.execute('''
                INSERT INTO "ELECTRONICS CATEGORY" VALUES ( :id, :name, :description, :image_src 
                )''', [id, name, description, image_src])
        conn.commit()
    conn.close()

def add_new_book_category(name , description):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                SELECT * FROM "BOOK CATEGORY" WHERE NAME =: name''',
                   [name])
    res = dict_fetch_all(cursor)
    if len(res) == 0:
        id = max_book_category_id() + 1
        cursor.execute('''
                        INSERT INTO "BOOK CATEGORY" VALUES ( :id, :name, :description
                        )''', [id, name, description])
        conn.commit()

    conn.close()

def add_new_author(name , profile):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT * FROM "AUTHOR" WHERE NAME =: name''',
                   [name])
    res = dict_fetch_all(cursor)
    if len(res) == 0:
        id = max_author_id() + 1
        cursor.execute('''
                            INSERT INTO "AUTHOR" VALUES ( :id, :name, :profile
                            )''', [id, name, profile])
        conn.commit()

    conn.close()

def add_publisher(name , phone_number , web_url , email , address):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT * FROM "PUBLISHER" WHERE NAME =: name''',
                   [name])
    res = dict_fetch_all(cursor)
    if len(res) == 0:
        id = max_publisher_id() + 1
        cursor.execute('''
                            INSERT INTO "PUBLISHER" VALUES ( :id, :name, :phone_number , :web_url,
                            :email , :address
                            )''', [id, name, phone_number , web_url , email , address])
        conn.commit()

    conn.close()


def add_new_book(isbn , title , edition , no_of_pages , country  ,language , price , image_src , summary , author , category , publisher , stock , sales_cnt=0):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''
                    SELECT * FROM "BOOK" WHERE TITLE =: title''',
                   [title])
    res = dict_fetch_all(cursor)
    print(title)
    if len(res) == 0:
        print("as")
        """If no author/ctg , they will be inserted"""
        author_id = get_author_id(author)
        pub_id = get_publisher_id(publisher)
        ctg_id = get_book_ctg_id(category)
        if(author_id==-1):
            add_new_author(author , "good")
            print(author)
        if(ctg_id==-1):
            add_new_book_category(category , "good one")

        id = max_book_id() + 1
        print(title)
        cursor.execute('''
                                INSERT INTO "BOOK" VALUES ( :id, :isbn, :title,
                                :edition , :no_of_pages , :country , :language , 
                                :price , :image_src , :summary , :author_id , :ctg_id , :pub_id , 
                                :stock , :sales_cnt)''', [id, isbn , title , edition , no_of_pages,
                                                          country , language , price , image_src ,
                                                          summary , author_id , ctg_id , pub_id ,
                                                          stock , sales_cnt])
        conn.commit()
    conn.close()
def get_author_id(name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select ID from MYSELF.AUTHOR where NAME=:name
        ''', [name]
    )
    res = dict_fetch_all(cursor)
    conn.close()
    if(len(res)>0):
        return res[0]['ID']
    else:
        return -1

def get_publisher_id(name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select ID from MYSELF.PUBLISHER where NAME =: name
        ''',[name]
    )
    res = dict_fetch_all(cursor)
    conn.close()
    if(len(res)>0):
        return res[0]['ID']
    else:
        return -1

def get_book_ctg_id(name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select ID from MYSELF."BOOK CATEGORY" where NAME =: name
        ''',[name]
    )
    res = dict_fetch_all(cursor)
    conn.close()
    if (len(res) > 0):
        return res[0]['ID']
    else:
        return -1

def get_comment_rating_cnts():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''
        select COUNT(c.ID) as ccnt  from MYSELF."COMMENT" c
        '''
    )
    res1 = dict_fetch_all(cursor)

    cursor = conn.cursor()
    cursor.execute(
        '''
        select COUNT(r.ID) as rcnt  from MYSELF."RATING" r
        '''
    )
    res2 = dict_fetch_all(cursor)
    print(res2)
    if (len(res1) > 0) and (len(res2) > 0):
        return res1[0]['CCNT'] , res2[0]['RCNT']
        #, res[0]['rcnt']
    else:
        return 0,0


if __name__ == "__main__":
    get_all_orders()