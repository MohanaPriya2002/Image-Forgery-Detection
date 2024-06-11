from django.db import models


class Admin_Details(models.Model):
    Username = models.CharField(default=None,max_length=100)
    Password = models.CharField(default=None,max_length=100)
    
    class Meta:
        db_table = 'Admin_Details'
                    


class User_details(models.Model):
    FirstName = models.CharField(default=None,max_length=100)
    LastName = models.CharField(default=None,max_length=100)
    Username = models.CharField(default=None,max_length=100)
    Email = models.CharField(default=None,max_length=100)
    Password = models.CharField(default=None,max_length=100)
    mobile = models.CharField(default=None,max_length=100)
    Address = models.CharField(default=None,max_length=100)
    City = models.CharField(default=None,max_length=100)
    State = models.CharField(default=None,max_length=100)
    ExpiryDate = models.DateField(default=None)
    ChatStatus = models.CharField(default=None,max_length=20)
    CreditCard = models.CharField(default=None,max_length=16) 
    Expiry = models.CharField(default=None,max_length=20)
    Cvv = models.CharField(default=None,max_length=3)
    
    class Meta:
        db_table = 'User_details'


class Stylish_details(models.Model):
    Name  = models.CharField(default=None,max_length=100)
    Contact = models.CharField(default=None,max_length=100)
    Address = models.CharField(default=None,max_length=100)
    Email = models.CharField(default=None,max_length=100)
    Username = models.CharField(default=None,max_length=100)
    Password = models.CharField(default=None,max_length=100)
    Speciality = models.CharField(default=None,max_length=100)
    Image1 = models.ImageField(upload_to='img/images')
    Image2 = models.ImageField(upload_to='img/images')
    Image3 = models.ImageField(upload_to='img/images')
    Image4 = models.ImageField(upload_to='img/images')
    Image5 = models.ImageField(upload_to='img/images')
    Status = models.CharField(default=None,max_length=100)

    class Meta:
        db_table = 'Stylish_details'


class Subscriptions(models.Model):
    halfyear  = models.IntegerField(default=None)
    year = models.IntegerField(default=None)
    
    class Meta:
        db_table = 'Subscriptions'




class Chat_details(models.Model):
    Type  = models.CharField(default=None,max_length=100)
    MsgFrom = models.CharField(default=None,max_length=100)
    Context = models.CharField(default=None,max_length=100)
    ContextImage = models.TextField(default=None)
    Uid = models.CharField(default=None,max_length=100)
    Sid = models.CharField(default=None,max_length=100)
    Datetime = models.DateTimeField() 

    class Meta:
        db_table = 'Chat_details'