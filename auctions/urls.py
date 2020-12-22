from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("cate", views.cate, name="cate"),
    path("remove", views.remove, name="remove"),
    path("closed/<int:id>", views.closed, name="closed"),
    path("cate/<category>", views.catelist, name="catelist"),
    path("new_list", views.new_list, name="new_list"),
    path("detail/<int:id>", views.detail, name="detail"),
    path("comnt/<int:id>", views.comnt, name="comnt"),
    path("bid_new/<int:id>", views.bid_new, name="bid_new"),
    path("watchlistview/<str:username>", views.watchlistview, name="watchlistview"),
    path("addwatchlist/<int:id>",views.addwatchlist, name="addwatchlist"),
    path("removewatchlist/<int:id>", views.removewatchlist, name="removewatchlist"),  
    
]



