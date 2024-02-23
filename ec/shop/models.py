from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default="")
    about=models.TextField(max_length=5000, default="")

    def __str__(self):
        return self.product_name
    
class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=70, default="")
    phone=models.IntegerField(default=0)
    desc=models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
    
class Order(models.Model):
    ord_id=models.AutoField(primary_key=True)
    items=models.CharField(max_length=5000, default="")
    name= models.CharField(max_length=100)
    email=models.CharField(max_length=70, default="")
    phone=models.IntegerField(default=0)
    address=models.CharField(max_length=200, default="")
    state=models.CharField(max_length=100, default="")
    city=models.CharField(max_length=100, default="")
    zipCode=models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    ord_id=models.IntegerField(default=0)
    update_desc=models.CharField(max_length=5000, default="")
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7]+"..."
    
class Login(models.Model):
    login_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    phone=models.IntegerField(default=0)
    email=models.CharField(max_length=70, default="")
    password=models.CharField(max_length=100,default="")
    address=models.CharField(max_length=200, default="")
    state=models.CharField(max_length=100, default="")
    city=models.CharField(max_length=100, default="")
    zipCode=models.IntegerField(default=0)

    def __str__(self):
        return self.email