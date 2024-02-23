from django.shortcuts import render
from .models import Product, Contact, Order,OrderUpdate, Login
# Create your views here.
thank=False
def index(request):
    products = Product.objects.all()
    # allprods=[[products, range(1,len(products))],
    #           [products, range(1,len(products))]]

    catProds = products.values('category', 'id')
    cats={item['category'] for item in catProds}
    
    allProds=[]
    for cat in cats:
        prod = products.filter(category=cat)
        for p in prod:
            p.disprice = int(p.price - (0.3 * p.price) - 1)
        allProds.append([prod, range(1, len(prod))])
    params = {'allprods': allProds}
    return render(request, 'shop/index.html', params)


def searchMatch(query,item):
    if query in item.desc or query in item.product_name or query in item.category:
        return True
    else:
        return False
        
def search(request):
    query=request.GET.get('search')
    products = Product.objects.all()
    # allprods=[[products, range(1,len(products))],
    #           [products, range(1,len(products))]]

    catProds = products.values('category', 'id')
    cats={item['category'] for item in catProds}
    
    allProds=[]
    for cat in cats:
        prod = products.filter(category=cat)
        pr=[item for item in prod if searchMatch(query, item)]
        for p in pr:
            p.disprice = int(p.price - (0.3 * p.price) - 1)
        if len(pr)!=0:
            allProds.append([pr, range(1, len(pr))])

    params = {'allprods': allProds}
    return render(request, 'shop/index.html', params)


def contact(request):
    if request.method=="POST":
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        phone= request.POST.get('phone', '')
        desc= request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')


def notifications(request):
    
    return render(request, 'shop/notifications.html')
logged=False
def account(request):
    loginSuccess=False
    emailNotFound=False
    WrongPassword=False
    log=Login.objects.all()
    logindata=log.values('email', 'password', 'name', 'phone', 'address', 'state', 'city', 'zipCode')
    if request.method=="POST":
        email=request.POST.get('email', '')
        password=request.POST.get('password', '')
        l=logindata.filter(email=email)
        if not l:
            emailNotFound=True
        else:
            if l[0]['password']==password:
                loginSuccess=True
                return render(request, 'shop/account.html', {'loginSuccess':loginSuccess, 'l':l[0]})
            else:
                WrongPassword=True
    return render(request, 'shop/account.html',{'emailNotFound':emailNotFound, 'WrongPassword': WrongPassword})

def login(request):


    return render(request, 'shop/login.html')

def signup(request):
    emailExists=False
    passwordNotMatch=False
    SignedIn=False
    log = Login.objects.all()
    logindata=log.values('email')
    if request.method=="POST":
        name=request.POST.get('name', '')
        phone=request.POST.get('phone', '')
        signemail=request.POST.get('signemail', '')
        signpassword=request.POST.get('signpassword', '')
        ComfirmPassword=request.POST.get('ConfirmPassword', '')
        address=request.POST.get('address', '')
        state=request.POST.get('state', '')
        city=request.POST.get('city', '')
        zipCode=request.POST.get('Zip_code', '')
        l=logindata.filter(email=signemail)
        if l:
            emailExists=True
        else:
            if signpassword==ComfirmPassword:
                login=Login(name=name, phone=phone, email=signemail, password=signpassword, address=address, state=state, city=city, zipCode=zipCode)
                login.save()
                SignedIn=True
            else:
                passwordNotMatch=True
    return render(request, 'shop/signup.html', {'emailExists': emailExists, 'passwordNotMatch':passwordNotMatch, 'SignedIn': SignedIn})

def forgot(request):
    
    return render(request, 'shop/forgot.html')



def cart(request):
    return render(request, 'shop/cart.html')


def productView(request,myid):
    product=Product.objects.filter(id=myid)
    for p in product:
            p.disprice = int(p.price - (0.3 * p.price) - 1)
    return render(request, 'shop/products.html', {'product': product[0]})

def placeOrder(request):
    if request.method=="POST":
        items=request.POST.get('itemsJson', '')
        name= request.POST.get('name', '')
        email= request.POST.get('email', '')
        phone= request.POST.get('phone', '')
        address= request.POST.get('address', '')
        state= request.POST.get('state', '')
        city= request.POST.get('city', '')
        zipcode= request.POST.get('Zip_code', '')
        order=Order(items=items, name=name, email= email, phone=phone, address= address, state=state, city=city, zipCode= zipcode)
        order.save()
        update=OrderUpdate(ord_id=order.ord_id, update_desc="Your Order has Been Confirmed")
        update.save()
        thank = True
        return render(request, 'shop/placeOrder.html', {'thank': thank, 'name': name})
    return render(request, 'shop/placeOrder.html')