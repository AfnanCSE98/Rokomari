from django.shortcuts import render
from miscellaneous.miscellaneous import *
from home.forms import *
import cx_Oracle
from bnbphoneticparser import BanglishToBengali
banglish2bengali = BanglishToBengali()
# Create your views here.
def is_electronic_category(ctg_name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."ELECTRONICS CATEGORY"
                                    WHERE "NAME" =: ctg_name''',
                   {'ctg_name':ctg_name})
    res = dict_fetch_all(cursor)
    if len(res)>0:
        return True
    else:
        return False;

def search(request):
    stxt = request.GET['search_txt']

    #if searched for a book or author
    if stxt[:3].isalnum():
        qtxt = banglish2bengali.parse(stxt.strip())
    else:
        qtxt = stxt
    print (qtxt)
    dict  =  get_dict(request , qtxt)
    return render(request , 'search_query/searchresult_book.html' , dict)


def get_dict(request , qtxt):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."BOOK"
                                WHERE "TITLE" =: qtxt''',
                   {'qtxt': qtxt})
    res = dict_fetch_all(cursor)
    if len(res)==0:
        return {}
    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['login_message'] = request.session.get('login_message')
    dict['cart_size'] = len(get_book_cart(request.session.get('id'))) + len(
        get_electronics_cart(request.session.get('id')))
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
    book['id'] = (res[0]['ID'])
    book['averageRating'] = get_average_rating(res[0]['ID'])
    book['userRating'] = get_customer_rating(dict['id'], res[0]['ID'])
    book['comments'] = get_comment(res[0]['ID'])
    book['image'] = res[0]['IMAGE_SRC']
    dict['theBook'] = book

    bookid = res[0]['ID']
    #Finding books of the same author
    author_id = res[0]['AUTHOR ID']
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.BOOK where "AUTHOR ID"=:author_id AND "ID"<>:bookid
        ''', [author_id , bookid]
    )
    res_author = dict_fetch_all(cursor)
    dict['author_book'] = res_author

    # Finding other books of the same ctg
    ctg_id = res[0]['CATEGORY ID']
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.BOOK where "CATEGORY ID" = :ctg_id AND "ID"<>:bookid AND "AUTHOR ID"<>:author_id
        ''', [ctg_id, bookid,author_id]
    )
    res_ctg = dict_fetch_all(cursor)
    conn.close()
    dict['ctg_book'] = res_ctg

    return dict