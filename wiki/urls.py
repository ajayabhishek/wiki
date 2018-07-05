from django.conf.urls import include,url
from django.contrib import admin
from rest_framework import routers
from blog import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from blog import views as blog_views
from django.urls import path
from rest_framework.authtoken import views





router = routers.DefaultRouter()
router.register(r'articles', blog_views.ArticleViewSet)


urlpatterns=[url(r'blog/',include('blog.urls')),
             url(r'^login/$', auth_views.login, {'template_name': 'blog/login.html'}, name='index'),
             url(r'^logout/$', auth_views.logout, {'next_page': '/blog/home'}, name='logout'),

             url(r'admin/', admin.site.urls),
             path('ckeditor/', include('ckeditor_uploader.urls')),
             path('addpost/', blog_views.showform, name='add_post'),
             url(r'', include(router.urls)), path('admin/', admin.site.urls,name='api_func'),

             #path('edit/post/<int:post_id>/', quiz_views.edit_post, name='edit_post'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    url(r'^api-token-auth/', views.obtain_auth_token)
]
