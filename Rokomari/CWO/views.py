from django.shortcuts import render
from miscellaneous.miscellaneous import *
from django.shortcuts import redirect
import cx_Oracle


# Create your views here.
#Cart Start


def cart(request):

    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = get_book_cart_len( dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])


    res = get_book_cart(request.session.get('id'))
    lst = []
    for item in res:
        """
        a, b, c = get_product_name_price(item['BOOK ID'])
        d = item['BOOK QUANTITY']
        """
        a, b, c, d = item['BOOK ID'], item['TITLE'], item['PRICE'], item['BOOK QUANTITY']
        lst.append((a, b, c, d))
    res = get_electronics_cart(request.session.get('id'))
    for item in res:
        """
        a, b, c = get_product_name_price(item['ELECTRONICS ID'])
        d = item['ELECTRONICS QUANTITY']
        """
        a, b, c, d = item['ELECTRONICS ID'], item['TITLE'], item['PRICE'], item['ELECTRONICS QUANTITY']
        lst.append((a, b, c, d))
    dict['cart'] = lst


    print(dict['cart'])
    total = 0
    for a, b, c, d in dict['cart']:
        total += int(c)
    dict['total'] = total

    return render(request, 'CWO/cart.html', dict)


def add_to_cart(request, product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    quantity = 1
    order_id = 1
    id = int(max_cart_id(product_id)) + 1;
    customer_id = request.session.get('id')
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT * FROM "MYSELF"."BOOK CART" WHERE "BOOK ID" =: product_id AND "USER ID" =: customer_id 
                        AND "ORDER ID" =: order_id''', { 'product_id' : product_id, 'customer_id' : customer_id, 'order_id' : order_id})
        res = dict_fetch_all(cursor)
        if len(res) == 0:
            cursor.execute('''
                                INSERT INTO "MYSELF"."BOOK CART"("ID", "USER ID", "BOOK ID", "BOOK QUANTITY", "ORDER ID")
                                VALUES( :id, :customer_id, :product_id, :quantity, :order_id)
                                ''', [id, customer_id, product_id, quantity, order_id])
    else:
        cursor.execute('''SELECT * FROM "MYSELF"."ELECTRONICS CART" WHERE "ELECTRONICS ID" =: product_id AND "USER ID" =: customer_id 
                                AND "ORDER ID" =: order_id''',
                       {'product_id': product_id, 'customer_id': customer_id, 'order_id': order_id})
        res = dict_fetch_all(cursor)
        if len(res) == 0:
            cursor.execute('''
                                        INSERT INTO "MYSELF"."ELECTRONICS CART"("ID", "USER ID", "ELECTRONICS ID", "ELECTRONICS QUANTITY", "ORDER ID")
                                        VALUES( :id, :customer_id, :product_id, :quantity, :order_id)
                                        ''', [id, customer_id, product_id, quantity, order_id])
    conn.commit()
    conn.close()
    if int(product_id) < THRESHOLD:
        return redirect('home:books:book_details', book_id=product_id)
    else:
        return redirect('home:electronics:electronics_details', electronics_id=product_id)


def delete_cart_item(request, product_id):
    customer_id = request.session.get('id')
    print(product_id + " " + str(customer_id))
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    order_id = 1
    if int(product_id) < THRESHOLD:
        cursor.execute('''DELETE FROM "MYSELF"."BOOK CART" WHERE "BOOK ID" =:product_id AND "USER ID" =:customer_id AND "ORDER ID" =: order_id
                        ''', {'product_id': product_id, 'customer_id': customer_id, 'order_id': order_id})
    else:
        cursor.execute('''DELETE FROM "MYSELF"."ELECTRONICS CART" WHERE "ELECTRONICS ID" =:product_id AND "USER ID" =:customer_id AND "ORDER ID" =: order_id
                                ''', {'product_id': product_id, 'customer_id': customer_id, 'order_id': order_id})
    conn.commit()
    conn.close()
    return redirect('/cart/')

def update_cart(request, product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    customer_id = request.session.get('id')
    quantity = request.GET.get(product_id)
    if int(product_id) < THRESHOLD:
        cursor.execute('''UPDATE "MYSELF"."BOOK CART" SET "BOOK QUANTITY" := quantity WHERE "BOOK ID" =: product_id AND "USER ID" =: customer_id AND "ORDER ID" =: order_id
                        ''', {'quantity': quantity, 'product_id':product_id, 'customer_id':customer_id, 'order_id': 1})
    else:
        cursor.execute('''UPDATE "MYSELF"."ELECTRONICS CART" SET "ELECTRONICS QUANTITY" := quantity WHERE "ELECTRONICS ID" =: product_id AND "USER ID" =: customer_id AND "ORDER ID" =: order_id
                                ''',
                       {'quantity': quantity, 'product_id': product_id, 'customer_id': customer_id, 'order_id': 1})
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/cart/')

#Cart End


#Wishlist Start


def wishlist(request):

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

    res = get_book_wishlist(dict['id'])
    lst = []
    for item in res:
        """
        lst.append(get_product_name_price(item['BOOK ID']))
        """
        lst.append((item['BOOK ID'], item['TITLE'], item['PRICE']))
    res = get_electronics_wishlist(dict['id'])
    for item in res:
        lst.append((item['ELECTRONICS ID'], item['TITLE'], item['PRICE']))
    dict['wishlist'] = lst

    print(dict['wishlist'])


    return render(request, 'CWO/wishlist.html', dict)


def add_to_wishlist(request, product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    customer_id = request.session.get('id')
    id = int(max_wishlist_id(product_id)) + 1;
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT * FROM "MYSELF"."BOOK WISHLIST" WHERE "BOOK ID" =: product_id AND "USER ID" =: customer_id 
                        ''',
                       {'product_id': product_id, 'customer_id': customer_id})
        res = dict_fetch_all(cursor)
        if len(res) == 0:
            cursor.execute('''
                                INSERT INTO "MYSELF"."BOOK WISHLIST"("ID", "USER ID", "BOOK ID")
                                VALUES( :id, :customer_id, :product_id)
                                ''', [id, customer_id, product_id])
    else:
        cursor.execute('''SELECT * FROM "MYSELF"."ELECTRONICS WISHLIST" WHERE "ELECTRONICS ID" =: product_id AND "USER ID" =: customer_id 
                                ''',
                       {'product_id': product_id, 'customer_id': customer_id})
        res = dict_fetch_all(cursor)
        if len(res) == 0:
            cursor.execute('''
                                        INSERT INTO "MYSELF"."ELECTRONICS WISHLIST"("ID", "USER ID", "ELECTRONICS ID")
                                        VALUES( :id, :customer_id, :product_id)
                                        ''', [id, customer_id, product_id])
    conn.commit()
    conn.close()
    if int(product_id) < THRESHOLD:
        return redirect('home:books:book_details', book_id=product_id)
    else:
        return redirect('home:electronics:electronics_details', electronics_id=product_id)


def add_to_cart_from_wishlist(request, product_id):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    quantity = 1
    order_id = 1
    id = int(max_cart_id(product_id)) + 1;
    customer_id = request.session.get('id')
    if int(product_id) < THRESHOLD:
        cursor.execute('''SELECT * FROM "MYSELF"."BOOK CART" WHERE "BOOK ID" =: product_id AND "USER ID" =: customer_id 
                            AND "ORDER ID" =: order_id''',
                       {'product_id': product_id, 'customer_id': customer_id, 'order_id': order_id})
        res = dict_fetch_all(cursor)
        if len(res) == 0:
            cursor.execute('''
                                    INSERT INTO "MYSELF"."BOOK CART"("ID", "USER ID", "BOOK ID", "BOOK QUANTITY", "ORDER ID")
                                    VALUES( :id, :customer_id, :product_id, :quantity, :order_id)
                                    ''', [id, customer_id, product_id, quantity, order_id])
    else:
        cursor.execute('''SELECT * FROM "MYSELF"."ELECTRONICS CART" WHERE "ELECTRONICS ID" =: product_id AND "USER ID" =: customer_id 
                                    AND "ORDER ID" =: order_id''',
                       {'product_id': product_id, 'customer_id': customer_id, 'order_id': order_id})
        res = dict_fetch_all(cursor)
        if len(res) == 0:
            cursor.execute('''
                                            INSERT INTO "MYSELF"."ELECTRONICS CART"("ID", "USER ID", "ELECTRONICS ID", "ELECTRONICS QUANTITY", "ORDER ID")
                                            VALUES( :id, :customer_id, :product_id, :quantity, :order_id)
                                            ''', [id, customer_id, product_id, quantity, order_id])
    conn.commit()
    conn.close()
    return redirect('/wishlist/')

def delete_wishlist_item(request, product_id):
    customer_id = request.session.get('id')
    print(product_id + " " + str(customer_id))
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        cursor.execute('''DELETE FROM "MYSELF"."BOOK WISHLIST" WHERE "BOOK ID" =:product_id AND "USER ID" =:customer_id
                        ''', {'product_id': product_id, 'customer_id': customer_id})
    else:
        cursor.execute('''DELETE FROM "MYSELF"."ELECTRONICS WISHLIST" WHERE "ELECTRONICS ID" =:product_id AND "USER ID" =:customer_id
                                ''', {'product_id': product_id, 'customer_id': customer_id})
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/wishlist/')


#Wishlist End



#order start


def order(request):

    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    customer_id = request.session.get('id')
    res1 = get_book_cart(customer_id)
    res2 = get_electronics_cart(customer_id)
    print(max_order_id())
    order_id = int(max_order_id()) + 1
    print("order_id :" + str(order_id))
    status = 'Pending'
    cursor.execute('''
                        INSERT INTO "MYSELF"."ORDER HISTORY"("ID" , "USER ID", "STATUS")
                        VALUES(:order_id,:customer_id,:status)
                        ''', [order_id, customer_id, status])
    #complex query
    for item in res1:
        quantity = request.GET.get(item['BOOK ID'])
        book_id = item['BOOK ID']
        cursor.execute('''
                            UPDATE "MYSELF"."BOOK CART"
                            SET "BOOK QUANTITY" = :quantity, "ORDER ID" = :order_id 
                            WHERE "BOOK ID" = :book_id AND "USER ID" = :customer_id  AND "ORDER ID" =:o
                            ''',
                       {'quantity': int(quantity),
                        'order_id': order_id,
                        'book_id': int(book_id),
                        'customer_id': int(customer_id),
                        'o': 1,
                        })
        book_sales = get_book_sales(book_id) + int(quantity)
        book_stock = get_book_stock(book_id) - int(quantity)
        cursor.execute('''
                            UPDATE "MYSELF".BOOK
                            SET "SALES COUNT" = :book_sales, STOCK = :book_stock 
                            WHERE "ID" = :book_id
                                    ''',
                       [book_sales, book_stock, book_id])
    for item in res2:
        quantity = request.GET.get(item['ELECTRONICS ID'])
        electronics_id = item['ELECTRONICS ID']
        cursor.execute('''
                            UPDATE "MYSELF"."ELECTRONICS CART"
                            SET "ELECTRONICS QUANTITY" = :quantity, "ORDER ID" = :order_id 
                            WHERE "ELECTRONICS ID" = :electronics_id AND "USER ID" = :customer_id  AND "ORDER ID" =:o
                            ''',
                       {'quantity': int(quantity),
                        'order_id': order_id,
                        'electronics_id': int(electronics_id),
                        'customer_id': int(customer_id),
                        'o': 1,
                        })
        electronics_sales = get_electronics_sales(electronics_id) + int(quantity)
        electronics_stock = get_electronics_stock(electronics_id) - int(quantity)
        cursor.execute('''
                            UPDATE "MYSELF".ELECTRONICS
                            SET "SALES COUNT" = :electronics_sales, STOCK = :electronics_stock 
                            WHERE "ID" = :electronics_id
                                            ''',
                       [electronics_sales, electronics_stock, electronics_id])
    conn.commit()
    conn.close()
    return redirect( 'home:CWO:specific_order', order_id=order_id)


def specific_order(request, order_id):

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
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

    res = get_book_cart(dict['id'], order_id)
    print(res)
    lst = []
    for item in res:
        """
        a, b, c = get_product_name_price(item['BOOK ID'])
        lst.append((a, b, c, item['BOOK QUANTITY']))
        """
        a, b, c, d = item['BOOK ID'], item['TITLE'], item['PRICE'], item['BOOK QUANTITY']
        lst.append((a, b, c, d))
    res = get_electronics_cart(dict['id'], order_id)
    for item in res:
        """
        a, b, c = get_product_name_price(item['ELECTRONICS ID'])
        lst.append((a, b, c, item['ELECTRONICS QUANTITY']))
        """
        a, b, c, d = item['ELECTRONICS ID'], item['TITLE'], item['PRICE'], item['ELECTRONICS QUANTITY']
        lst.append((a, b, c, d))
    dict['specificOrder'] = lst
    print(dict['specificOrder'])


    total = 0
    for a, b, c, d in dict['specificOrder']:
        total += int(c) * int(d)
    dict['total'] = total
    dict['status'] = get_order_status(order_id)


    return render(request, 'CWO/specificOrder.html', dict)


def all_order(request):

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


    res = get_order_ids(dict['id'])
    lst = []
    for item in res:
        lst.append(int(item['ID']))
    lst.sort(reverse=True)
    f_list = []
    for it in lst:
        res1 = get_book_cart( dict['id'], it)
        res2 = get_electronics_cart( dict['id'], it)
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
            total += int(c)*int(d)
        p['total'] = total
        p['lst'] = lt
        p['status'] = get_order_status(it)
        p['order_id'] = it
        f_list.append(p)
    dict['allOrderItems'] = f_list
    return render(request, 'CWO/allOrders.html', dict)


#order end