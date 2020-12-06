from django.shortcuts import render
from miscellaneous.miscellaneous import *
from django.shortcuts import redirect
import cx_Oracle


# Create your views here.


def give_rating(request, product_id):
    id = int(max_rating_id()) + 1
    stars = request.GET.get(product_id)
    print(stars)
    customer_id = request.session.get('id')
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    print(product_id)
    print(id)
    if int(product_id) < THRESHOLD:
        cursor.execute('''DELETE FROM "MYSELF"."RATING"
                               WHERE "BOOK ID" =: product_id AND "USER ID" =: customer_id''',
                   {'product_id': product_id, 'customer_id': customer_id})
        cursor.execute('''
                        INSERT INTO "MYSELF"."RATING"("ID", "STARS", "BOOK ID", "USER ID")
                        VALUES(:id, :stars, :product_id, :customer_id)
                        ''', [id, stars, product_id, customer_id])
    else:
        cursor.execute('''DELETE FROM "MYSELF"."RATING"
                                       WHERE "ELECTRONICS ID" =: product_id AND "USER ID" =: customer_id''',
                       {'product_id': product_id, 'customer_id': customer_id})
        cursor.execute('''
                                INSERT INTO "MYSELF"."RATING"("ID", "STARS", "ELECTRONICS ID", "USER ID")
                                VALUES(:id, :stars, :product_id, :customer_id)
                                ''', [id, stars, product_id, customer_id])
    conn.commit()
    conn.close()
    if int(product_id) < THRESHOLD:
        return redirect('home:books:book_details', book_id=product_id)
    else:
        return redirect('home:electronics:electronics_details', electronics_id=product_id)


def add_comment(request, product_id):
    id = int(max_comment_id()) + 1
    pcomment = request.GET.get(product_id)
    print(pcomment)
    customer_id = request.session.get('id')
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    if int(product_id) < THRESHOLD:
        id = 5000
        cursor.execute('''
                    INSERT INTO "MYSELF"."COMMENT"("ID", "DESCRIPTION", "BOOK ID", "USER ID")
                    VALUES( :id, :pcomment, :product_id, :customer_id)
                    ''', [id, pcomment, product_id, customer_id])
    else:
        id = 5000
        cursor.execute('''
                            INSERT INTO "MYSELF"."COMMENT"("ID", "DESCRIPTION", "ELECTRONICS ID", "USER ID")
                            VALUES( :id, :pcomment, :product_id, :customer_id)
                            ''', [id, pcomment, product_id, customer_id])
    conn.commit()
    conn.close()
    if int(product_id) < THRESHOLD:
        return redirect('home:books:book_details', book_id=product_id)
    else:
        return redirect('home:electronics:electronics_details', electronics_id=product_id)
