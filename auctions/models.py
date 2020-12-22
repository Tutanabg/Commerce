from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime





CATEGORY_CHOICES = (
        ('books','BOOKS'), 
        ('cars', 'CARS'), 
        ('electronics','ELECTRONICS'), 
        ('fashion','FASHION'),
        ('houses','HOUSES'),
        ('toys','TOYS')
     )





class User(AbstractUser):
    pass
    
    



class list(models.Model): 
   posted_by = models.ForeignKey(User, on_delete=models.CASCADE, default=User.username)
   title = models.CharField(max_length=100) 
   image = models.ImageField(blank=True, null=True) 
   description = models.CharField(max_length = 300)    
   starting_bid = models.IntegerField(null=True) 
   category = models.CharField(max_length=15, choices=CATEGORY_CHOICES, default='books')
   date_posted = models.DateTimeField(auto_now_add=True, blank=True) 
   def __int__(self):
         return self.id
         
        

class comments(models.Model): 
     user_id= models.CharField(max_length=50) 
     list_id = models.CharField(max_length=50) 
     message = models.TextField() 
     def __repr__(self):
         return self.message

      
	
class bid(models.Model): 
	user_id = models.CharField(max_length=50, null=True)
	title = models.CharField(max_length=50, null=True)
	bid = models.IntegerField(null=True) 
	list_id = models.IntegerField()
	def __int__(self):
         return self.bid
         
         
class watchlist(models.Model):
    user = models.CharField(max_length=64)
    list_id = models.IntegerField()
    title = models.CharField(max_length=64, null=True)
    image = models.ImageField(blank=True, null=True)
    
    



