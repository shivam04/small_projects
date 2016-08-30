from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', "djangotask.views.home",name="home"),
	url(r'^register/$', "djangotask.views.register",name="register"),
	url(r'^login/$', "djangotask.views.user_login",name="login"),
	url(r'^logout/$', "djangotask.views.user_logout",name="logout"),
	url(r'^register/autocomplete/$', "djangotask.views.autocomplete",name="autocomplete"),
]
