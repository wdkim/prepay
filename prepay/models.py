from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.name    
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    #seller = models.ForeignKey(Seller)
    picture = models.ImageField(upload_to='%Y/%m/%d')
    categories = models.ManyToManyField(Category)
    description = models.TextField(max_length=1000)

    def purchase(self):
        return str("sold!")

    def get_picture_url(self):
        return str(self.picture.url)

    def __unicode__(self):
        return self.name

'''
I'm implementing these user classes, possibly just for version 0
convenience.  We need to reconcile this with using the Admin site
for users, roles, permissions, etc.
'''
class User(models.Model):
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    
    name = models.CharField(max_length=60)
    
    def __unicode__(self):
        return self.name

class Seller(User):
    products = models.ManyToManyField(Product) #todo: filter by owner
    #products = product_set.all()
    
    #we might want to check out https://github.com/dcramer/django-ratings
    CHOICES = [(i,i) for i in range(6)]
    rating = models.IntegerField(choices=CHOICES)

class Listing(models.Model):
    name = models.CharField(max_length=50)
    seller = models.ForeignKey(Seller)
    product = models.ForeignKey(Product)
    description = models.TextField(max_length=1000)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def offer(self):
        return str("offered!")
    
    def withdraw(self):
        return str("withdrawn!")
    
    def __unicode__(self):
        return self.name
    
class Bank(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    
class Escrow(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
    
class Listing(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name