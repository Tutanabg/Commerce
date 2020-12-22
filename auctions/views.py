from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


post = list.objects.all()


def index(request):
     return render(request, "auctions/index.html", { "list":post})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


@login_required
def new_list(request): 
     form = ListForm(request.POST) 
     if form.is_valid(): 
         form.save() 
         return render(request, "auctions/list.html", {"form":form}) 
     else:
         return render(request, "auctions/list.html", {
      "form":ListForm()
        }) 


@login_required
def watchlistview(request, username):
	p = watchlist.objects.filter(user=username)
	return render(request, "auctions/watchlist.html", {"page":p, "list":post}) 
    
@login_required
def catelist(request, category): 
     data=  list.objects.filter(category=category)  
     return render(request, "auctions/category.html", {
      "data":data, "post":category.capitalize(), 
        }) 


@login_required
def cate(request): 
      return render(request, "auctions/categorylist.html") 
      
@login_required
def unauthorized(request): 
      return render(request, "auctions/unauthorized.html") 

@login_required
def bid_new(request, id):
	data = list.objects.get(pk=id)
	bdn = bid()
	bdn.user_id = request.user.username
	bdn.title = data.title
	bdn.bid = request.POST.get('bid')
	bdn.list_id = data.id
	bdn.save()
	b = bid.objects.filter(list_id=id)
	bd = b.last()
	c = comments.objects.filter(list_id=id)
	return render(request, "auctions/detail.html", {"data":data, "bd":bd, "c":c})
     	
@login_required
def comnt (request, id):
	data = list.objects.get(pk=id)
	com = comments()
	com.user_id = request.user.username
	com.list_id = id
	com.message = request.POST.get('message')
	com.save()
	c = comments.objects.filter(list_id=id)
	b = bid.objects.filter(list_id=id)
	bd = b.last()
	return render(request, "auctions/detail.html", {"c":c, "data":data, "bd":bd})
    


@login_required
def detail(request, id):
     data= list.objects.get(pk=id)
     cont = comments.objects.filter(list_id=id)
     b = bid.objects.filter(list_id=id)
     bd = b.last()
     return render(request, "auctions/detail.html", {
      "data":data, "comment":cont, "bd":bd, 
        }) 
     

@login_required 
def addwatchlist(request, id): 
	da = list.objects.get(pk=id)
	m = watchlist()
	m.user = request.user.username
	m.list_id = id
	m.title = da.title
	m.image = da.image
	m.save()
	return redirect('index')


@login_required
def removewatchlist(request, id): 
           w = watchlist.objects.filter(user=request.user.username, list_id=id)
           w.delete() 
           return redirect('remove')
           

@login_required
def remove(request): 
          return render(request, "auctions/removewatchlist.html")   
 
           
@login_required
def closebid(request, id):
      close = list.objects.get(id=id)
      close.delete()
      return redirect('closed')
      
@login_required
def closed(request, id):
	winner=list.objects.get(id=id)
	b = bid.objects.filter(list_id=id)
	bd = b.last()
	return render(request, "auctions/closed.html",{"winner":winner, "bid":bd})  
    
        

   
        
      
 
     
