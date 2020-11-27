from django.shortcuts import render
from .forms import *
from miscellaneous.miscellaneous import *
from django.shortcuts import redirect


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


