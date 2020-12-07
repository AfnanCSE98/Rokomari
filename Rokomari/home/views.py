from django.shortcuts import render
from .forms import *
from miscellaneous.miscellaneous import *
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import reverse

# Create your views here.
def index(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if authenticate(username, password):
                all_customers = all_users()
                dict = get_current_customer(all_customers, username)
                print(username)
                request.session['username'] = dict['NAME']
                request.session['id'] = dict['ID']
                request.session['mobile'] = dict['PHONE NUMBER']
                request.session['email'] = dict['EMAIL']
                request.session['address'] = dict['ADDRESS']
                #request.session['password'] = dict['PASSWORD']
                request.session['account_type'] = dict['TYPES']
                request.session['login_message'] = "Login Successful! Welcome, "+dict['NAME']
                return redirect('/home/')
            else:
                form = LoginForm()
                dict = {}
                dict['login_message'] = "Login Failed! Sorry"
                dict['form'] = form
                return render(request, 'home/index.html', dict)
    else:
        request.session.flush()
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})

def home(request):
    if 'username' in request.session:
        dict={}
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
        dict['bestseller'] = bestseller()
        return render(request, 'home/home.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            if check_username(username):
                form = UserForm()
                request.session['login_message'] = 'Duplicate Name, Please try another'
                return render(request, 'home/signup.html', {'form': form})
            if check_email(email):
                form = UserForm()
                request.session['login_message'] = 'Duplicate Email, Please try another'
                return render(request, 'home/signup.html', {'form': form})
            id = int(max_customer_id())
            id = id + 1
            print("******")
            print(id)
            create_customer(id, username, email, mobile, address, password, 'C')
            all_customers = all_users()
            dict = get_current_customer(all_customers, username)
            request.session['username'] = dict['NAME']
            request.session['id'] = dict["ID"]
            request.session['mobile'] = dict['PHONE NUMBER']
            request.session['email'] = dict['EMAIL']
            request.session['address'] = dict['ADDRESS']
            #request.session['password'] = dict['PASSWORD']
            request.session['account_type'] = dict['TYPES']
            request.session['login_message'] = "Congratulations " + dict['NAME'] + ", Sign Up Successful"
            return redirect('/home/')
    else:
        form = UserForm()
    return render(request, 'home/signup.html', {'form': form})

def user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            id = request.session.get('id')  #"getting current customer's id"

            update_customer(id, username, email, mobile, address, password)
            all_customers = all_users()
            dict = get_current_customer(all_customers, username)
            request.session['username'] = dict['NAME']
            request.session['id'] = dict["ID"]
            request.session['mobile'] = dict['PHONE NUMBER']
            request.session['email'] = dict['EMAIL']
            request.session['address'] = dict['ADDRESS']
            request.session['password'] = password
            request.session['account_type'] = dict['TYPES']

            form = UserProfileForm()
            form.fields['username'].initial = dict['NAME']
            form.fields['password'].initial = '*'*len(password)
            form.fields['email'].initial = dict['EMAIL']
            form.fields['mobile'].initial = dict['PHONE NUMBER']
            form.fields['account_type'].initial = dict['TYPES']
            form.fields['address'].initial = dict['ADDRESS']

            s = {'username': dict['NAME'], 'mobile': dict['PHONE NUMBER'], 'email': dict['EMAIL'], 'address': dict['ADDRESS'],
                 'account_type': dict['TYPES'], 'password': password, 'form': form,
                 'cart_size': len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id'))),
                 'wishlist_size' : len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))}

            s['all_orders'] = get_orders_of_this_user(dict["ID"])

            return render(request, 'home/user_profile.html', s)
    elif 'username' in request.session:
        dict = {'username': request.session.get('username'), 'id': request.session.get('id'),
                'mobile': request.session.get('mobile'), 'email': request.session.get('email'),
                'address': request.session.get('address'), 'account_type': request.session.get('account_type'),
                'password': request.session.get('password'), 'cart_size': len(get_book_cart(request.session.get('id'))) + len(get_electronics_cart(request.session.get('id'))),
                'wishlist_size' : len(get_book_wishlist(request.session.get('id'))) + len(get_electronics_wishlist(request.session.get('id')))}
        form = UserProfileForm()
        form.fields['username'].initial = dict['username']
        form.fields['password'].initial = dict['password']
        form.fields['email'].initial = dict['email']
        form.fields['mobile'].initial = dict['mobile']
        form.fields['account_type'].initial = dict['account_type']
        form.fields['address'].initial = dict['address']
        dict['form'] = form

        dict['all_orders'] = get_orders_of_this_user(dict['id'])
        print(dict['all_orders'])

        return render(request, 'home/user_profile.html', dict)
    else:
        form = LoginForm()
        return render(request, 'home/index.html', {'form': form})



def admin_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if is_admin(username, password):
                all_customers = all_users()
                dict = get_current_customer(all_customers, username)
                print("Hi admin " + username)
                request.session['username'] = dict['NAME']
                request.session['id'] = dict['ID']
                request.session['mobile'] = dict['PHONE NUMBER']
                request.session['email'] = dict['EMAIL']
                request.session['address'] = dict['ADDRESS']
                #request.session['password'] = dict['PASSWORD']
                request.session['account_type'] = dict['TYPES']
                request.session['login_message'] = "Login Successful! Welcome, "+dict['NAME']
                return redirect('/admindashboard/')
            else:
                form = LoginForm()
                dict = {}
                dict['login_message'] = "Login Failed! Sorry"
                dict['form'] = form
                return render(request, 'home/admin_login.html', dict)
    else:
        request.session.flush()
        form = LoginForm()
        return render(request, 'home/admin_login.html', {'form': form})

def admin(request):
    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

    x,y =  get_comment_rating_cnts()
    dict['no_of_comment'] = x
    dict['no_of_rating']  = y
    print(dict)

    return render(request, 'home/admin.html', dict)

def add_electronics(request):
    if request.method == "POST":
        form = AddElectronicsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            model = form.cleaned_data['model']
            price = form.cleaned_data['price']
            image_src = form.cleaned_data['image_src']
            description = form.cleaned_data['description']
            warranty = form.cleaned_data['warranty']
            category = form.cleaned_data['category']
            brand = form.cleaned_data['brand']
            number_of_items_added = form.cleaned_data['number_of_items_added']
            brand_id = get_brand_id(brand)
            category_id = get_electronics_category_id(category)
            if isinstance(brand_id, type(None)) or isinstance( category_id, type(None)):
                dict = {}
                dict['username'] = request.session.get('username')
                dict['id'] = request.session.get('id')
                dict['mobile'] = request.session.get('mobile')
                dict['email'] = request.session.get('email')
                dict['address'] = request.session.get('address')
                dict['account_type'] = request.session.get('account_type')
                dict['password'] = request.session.get('password')
                dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
                dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
                dict['form'] = AddElectronicsForm()
                return render(request, 'home/add_electronics.html', dict)
            print(description)
            adding_electronics(title, model, price, image_src, description, warranty, category_id, brand_id, number_of_items_added)
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddElectronicsForm()
            return render( request, 'home/add_electronics.html', dict)
        else:
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddElectronicsForm()
            return render(request, 'home/add_electronics.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = AddElectronicsForm()
        return render(request, 'home/add_electronics.html', dict)

def update_electronics(request):
    if request.method == "POST":
        form = UpdateElectronicsForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            model = form.cleaned_data['model']
            price = form.cleaned_data['price']
            warranty = form.cleaned_data['warranty']
            brand = form.cleaned_data['brand']
            number_of_items_added = form.cleaned_data['number_of_items_added']
            brand_id = get_brand_id(brand)
            if isinstance(brand_id, type(None)):
                dict = {}
                dict['username'] = request.session.get('username')
                dict['id'] = request.session.get('id')
                dict['mobile'] = request.session.get('mobile')
                dict['email'] = request.session.get('email')
                dict['address'] = request.session.get('address')
                dict['account_type'] = request.session.get('account_type')
                dict['password'] = request.session.get('password')
                dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
                dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
                dict['form'] = AddElectronicsForm()
                return render(request, 'home/add_electronics.html', dict)
            updating_electronics(title, model, price, warranty, brand_id, number_of_items_added)
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = UpdateElectronicsForm()
            return render( request, 'home/update_electronics.html', dict)
        else:
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = UpdateElectronicsForm()
            return render(request, 'home/update_electronics.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = UpdateElectronicsForm()
        return render(request, 'home/update_electronics.html', dict)

def add_brand(request):
    if request.method == "POST":
        form = AddBrandForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            web_url = form.cleaned_data['web_url']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            image_src = form.cleaned_data['image_src']
            adding_brand( name, phone_number, web_url, email, address, image_src)
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddBrandForm()
            return render(request, 'home/add_brand.html', dict)
        else:
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddBrandForm()
            return render(request, 'home/add_brand.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = AddBrandForm()
        return render(request, 'home/add_brand.html', dict)

def add_electronics_category(request):
    if request.method == "POST":
        form = AddElectronicsCategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            image_src = form.cleaned_data['image_src']
            adding_electronics_category(name, description, image_src)
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddElectronicsCategoryForm()
            return render(request, 'home/add_electronics_category.html', dict)
        else:
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddElectronicsCategoryForm()
            return render(request, 'home/add_electronics_category.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = AddElectronicsCategoryForm()
        return render(request, 'home/add_electronics_category.html', dict)

def add_publisher(request):
    pass

def add_author(request):
    if request.method == "POST":
        form = AddAuthor_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            profile = form.cleaned_data['profile']

            add_new_author(name , profile)
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddAuthor_Form()
            return render(request, 'home/add_author.html', dict)
        else:
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddAuthor_Form()
            return render(request, 'home/add_author.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = AddAuthor_Form()
        return render(request, 'home/add_author.html', dict)

def add_book_category(request):
    if request.method == "POST":
        form = AddCategory_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            add_new_book_category(name , description)
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddCategory_Form()
            return render(request, 'home/add_category.html', dict)
        else:
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = AddCategory_Form()
            return render(request, 'home/add_category.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = AddCategory_Form()
        return render(request, 'home/add_category.html', dict)


def add_book(request):
    if request.method == "POST":
        form = Addbook_Form(request.POST)
        print(form.errors)
        if form.is_valid():
            isbn = form.cleaned_data['ISBN']
            title = form.cleaned_data['Title']
            edition = form.cleaned_data['Edition']
            country = form.cleaned_data['Country']
            price = form.cleaned_data['Price']
            image_src = form.cleaned_data['Image_src']
            summary = form.cleaned_data['Summary']
            no_of_pages = form.cleaned_data['No_of_Pages']
            category = form.cleaned_data['Category']
            author = form.cleaned_data['Author']
            publisher = form.cleaned_data['Publisher']
            language = form.cleaned_data['Language']
            stock = form.cleaned_data['Stock']

            pub_id = get_publisher_id(publisher)
            print(pub_id)
            if pub_id==-1:
                print("pub nai")
                dict = {}
                dict['username'] = request.session.get('username')
                dict['id'] = request.session.get('id')
                dict['mobile'] = request.session.get('mobile')
                dict['email'] = request.session.get('email')
                dict['address'] = request.session.get('address')
                dict['account_type'] = request.session.get('account_type')
                dict['password'] = request.session.get('password')
                dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
                dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
                dict['form'] = Addbook_Form()
                return render(request, 'home/add_book.html', dict)

            add_new_book(isbn , title , edition , no_of_pages , country ,
                     language , price ,image_src , summary , author , category , publisher,
                     stock)
            print("done")
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = Addbook_Form()
            return render( request, 'home/add_book.html', dict)
        else:
            print("form valid na")
            dict = {}
            dict['username'] = request.session.get('username')
            dict['id'] = request.session.get('id')
            dict['mobile'] = request.session.get('mobile')
            dict['email'] = request.session.get('email')
            dict['address'] = request.session.get('address')
            dict['account_type'] = request.session.get('account_type')
            dict['password'] = request.session.get('password')
            dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
            dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
            dict['form'] = Addbook_Form()
            return render(request, 'home/add_book.html', dict)
    else:
        dict = {}
        dict['username'] = request.session.get('username')
        dict['id'] = request.session.get('id')
        dict['mobile'] = request.session.get('mobile')
        dict['email'] = request.session.get('email')
        dict['address'] = request.session.get('address')
        dict['account_type'] = request.session.get('account_type')
        dict['password'] = request.session.get('password')
        dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
        dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])
        dict['form'] = Addbook_Form()
        return render(request, 'home/add_book.html', dict)


def all_books(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT ID, TITLE, (SELECT "NAME" FROM MYSELF."BOOK CATEGORY" C WHERE C.ID = B."CATEGORY ID") CATEGORY_NAME,
                                        (SELECT "NAME" FROM MYSELF.PUBLISHER P WHERE P.ID = B."PUBLISHER ID") PUBLISHER_NAME,
                                        (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."BOOK ID" = B.ID) "AVERAGE RATING",
                                        IMAGE_SRC,    PRICE FROM MYSELF.BOOK B 
                        ''')
    res = dict_fetch_all(cursor)
    conn.close()

    for item in res:
        if not isinstance(item['AVERAGE RATING'], type(None)):
            item['star_list'] = get_star_list(int(item['AVERAGE RATING']))

    dict = {}
    dict['book'] = res
    #dict['author_name'] = get_author_name(author_id)
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    #dict['author_id'] = author_id
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

    return render(request, 'home/all_books.html', dict)


def all_electronics(request):
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCLPDB')
    conn = cx_Oracle.connect(user='MYSELF', password='123', dsn=dsn_tns)
    cursor = conn.cursor()
    cursor.execute('''SELECT ID, TITLE, PRICE,  
                                (SELECT B.NAME FROM MYSELF.BRAND B WHERE B.ID = E."BRAND ID") BRAND_NAME,
                                (SELECT  ROUND(AVG(TO_NUMBER(STARS))) FROM RATING R WHERE R."ELECTRONICS ID" = E.ID) "AVERAGE RATING",
                                IMAGE_SRC FROM MYSELF.ELECTRONICS E 
                            ''')
    res = dict_fetch_all(cursor)
    conn.close()

    for item in res:
        if not isinstance(item['AVERAGE RATING'], type(None)):
            item['star_list'] = get_star_list(int(item['AVERAGE RATING']))

    dict = {}
    dict['electronics'] = res
    #dict['category_name'] = get_electronics_category_name(ctg_id)
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

    return render(request, 'home/all_electronics.html', dict)


def all_orders(request):
    dict = {}
    dict['username'] = request.session.get('username')
    dict['id'] = request.session.get('id')
    dict['mobile'] = request.session.get('mobile')
    dict['email'] = request.session.get('email')
    dict['address'] = request.session.get('address')
    dict['account_type'] = request.session.get('account_type')
    dict['password'] = request.session.get('password')
    dict['cart_size'] = get_book_cart_len(dict['id'], 1) + get_electronics_cart_len(dict['id'], 1)
    dict['wishlist_size'] = get_book_wishlist_len(dict['id']) + get_electronics_wishlist_len(dict['id'])

    orders = get_all_orders()
    dict['all_orders'] = orders
    dict['form'] = DeliveredForm()

    #form = DeliveredForm(request.POST or None)
    if request.method == 'POST' :
        kotono = int(request.POST.get('kotono'))
        print(type(kotono))
        # is_delivered = form.cleaned_data['delivered']
        # if is_delivered:
        c = 1
        for i in orders:
            if c == kotono:
                update_order_status(i['order_id'])
                break
            c = c + 1
        #return HttpResponseRedirect(reverse('all_orders'))
        return redirect('/all-orders')

    return render(request, 'home/all_orders.html', dict)


