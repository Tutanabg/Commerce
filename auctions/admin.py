from django.contrib import admin
from .models import User, list, bid, comments, watchlist
# Register your models here.
admin.site.register(User) 
admin.site.register(list) 
admin.site.register(bid)
admin.site.register(comments)
admin.site.register(watchlist)

     

