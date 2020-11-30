from django.shortcuts import render
from miscellaneous.miscellaneous import *
from home.forms import *
import cx_Oracle
from bnbphoneticparser import BanglishToBengali
banglish2bengali = BanglishToBengali()
# Create your views here.
def is_electronic_category(ctg_name):
    ctg_name = ctg_name.lower()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."ELECTRONICS CATEGORY"
                                    WHERE LOWER("NAME") =: ctg_name''',
                   {'ctg_name':ctg_name})
    res = dict_fetch_all(cursor)
    if len(res)>0:
        return True
    else:
        return False;


def is_author(author_name):
    #author_name = author_name.lower()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select * from  MYSELF.BOOK b 
           WHERE b."AUTHOR ID" = (SELECT ID FROM MYSELF.AUTHOR WHERE NAME = :author_name) 
        ''',[author_name]
    )
    res = dict_fetch_all(cursor)
    conn.close()
    if len(res)>0:
        return True
    else:
        return False;

def search(request):
    stxt = request.GET['search_txt']
    if is_electronic_category(stxt):
        e_dict = get_dict_electronic_ctg(request , stxt)
        return render(request, 'search_query/searchresult_electronics.html', e_dict)

    #if searched for a book or author
    if stxt[:3].isalnum():
        qtxt = banglish2bengali.parse(stxt.strip())
    else:
        qtxt = stxt
    print (qtxt)
    if(is_author(qtxt)):
        a_dict = get_dict_author(request , qtxt)
        return render(request, 'search_query/searchresult_author.html', a_dict)
    b_dict = get_dict_book(request , qtxt)
    return render(request , 'search_query/searchresult_book.html' , b_dict)


def get_dict_author(request , author_name):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute(
        '''select b.ID , b.TITLE , b.PRICE , b.IMAGE_SRC from  MYSELF.BOOK b 
           WHERE b."AUTHOR ID" = (SELECT ID FROM MYSELF.AUTHOR WHERE NAME = :author_name) 
        ''', [author_name]
    )
    res = dict_fetch_all(cursor)
    for item in res:
        averageRating = get_average_rating(item['ID'])
        if not isinstance(averageRating, type(None)):
            item['star_list'] = get_star_list(int(averageRating))
    print(res)
    if(len(res)==0):
        return {}

    dict = user_details(request)
    dict['book'] = res
    dict['author_name'] = author_name

    # all authors
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.AUTHOR 
        '''
    )
    res = dict_fetch_all(cursor)
    conn.close()
    author_id = [x['ID'] for x in res]
    author_name = [x['NAME'] for x in res]
    dict['all_authors'] = [(x[0], x[1]) for x in zip(author_id, author_name)]
    return dict
def get_dict_electronic_ctg(request , ctg_name):
    ctg_name = ctg_name.lower()
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    # complex query can be done here
    cursor.execute(
        '''SELECT e.ID , e.TITLE , e.MODEL , e.PRICE , e.DESCRIPTION , e."IMAGE_SRC" , e."BRAND ID" FROM "MYSELF"."ELECTRONICS" e , "MYSELF"."ELECTRONICS CATEGORY" ec 
           where e."CATEGORY ID" = ec."ID" AND LOWER(ec."NAME") = :ctg_name
        ''', [ctg_name]
    )
    res = dict_fetch_all(cursor)
    if len(res)==0:
        return {}
    for electronics in res:
        electronics['BRAND_NAME'] = get_brand_name(electronics['BRAND ID'])
        average_rating = get_average_rating(electronics['ID'])
        if not isinstance(average_rating, type(None)):
            electronics['star_list'] = get_star_list(int(average_rating))
    dict = user_details(request)
    dict['electronics'] = res
    dict['ctg_name'] = ctg_name

    #taking all categories of electronics
    cursor = conn.cursor()
    cursor.execute('''SELECT ID , NAME FROM MYSELF."ELECTRONICS CATEGORY"''')
    res = dict_fetch_all(cursor)
    conn.close()
    ctg_id = [x['ID'] for x in res]
    ctg_name = [x['NAME'] for x in res]
    dict['all_categories'] = [(x[0], x[1]) for x in zip(ctg_id, ctg_name)]
    return dict

def get_dict_book(request , qtxt):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM "MYSELF"."BOOK"
                                WHERE "TITLE" =: qtxt''',
                   {'qtxt': qtxt})
    res = dict_fetch_all(cursor)
    if len(res)==0:
        return {}

    dict = user_details(request)

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
    if not isinstance(book['averageRating'], type(None)):
        book['star_list'] = get_star_list(int(book['averageRating']))
    if not isinstance(book['userRating'], type(None)):
        book['star_list_user'] = get_star_list(int(book['userRating']))
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
    for item in res_author:
        averageRating = get_average_rating(item['ID'])
        if not isinstance(averageRating, type(None)):
            item['star_list'] = get_star_list(int(averageRating))
    dict['author_book'] = res_author

    # Finding other books of the same ctg
    ctg_id = res[0]['CATEGORY ID']
    cursor = conn.cursor()
    cursor.execute(
        '''select * from MYSELF.BOOK where "CATEGORY ID" = :ctg_id AND "ID"<>:bookid AND "AUTHOR ID"<>:author_id
        ''', [ctg_id, bookid,author_id]
    )
    res_ctg = dict_fetch_all(cursor)
    for item in res_ctg:
        averageRating = get_average_rating(item['ID'])
        if not isinstance(averageRating, type(None)):
            item['star_list'] = get_star_list(int(averageRating))
    dict['ctg_book'] = res_ctg

    cursor = conn.cursor()
    cursor.execute(
        '''select ID , NAME from MYSELF."BOOK CATEGORY"'''
    )
    res = dict_fetch_all(cursor)
    conn.close()
    ctg_ID = [x['ID'] for x in res]
    ctg_NAME = [x['NAME'] for x in res]
    dict['all_categories'] = [(x[0], x[1]) for x in zip(ctg_ID, ctg_NAME)]

    return dict

def user_details(request):
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

    return dict