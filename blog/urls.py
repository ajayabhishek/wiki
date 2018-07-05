from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views as auth_views
from . import views as core_views


from . import views

urlpatterns=[url(r'idx',views.index,name='index'),
             url(r'home', views.home, name='index'),
             url(r'sc',views.school,name='index'),
             url(r'profile', views.profile_view, name='index'),

             url(r'^signup/$', core_views.signup, name='signup'),

             url(r'blogform',views.showform,name='index'),
             url(r'blogshow',views.showstudent,name='index'),
             ]
