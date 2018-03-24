"""proje URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth import views as auth_views
from blog import views
from proje import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<url>[^/]*)/$',views.detail, name ='detail'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^register/',views.register, name='register'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^change_password/$', auth_views.password_change, name='password_change'),
    url(r'^change_password/done/', auth_views.password_change_done, name='password_change_done'),
]

urlpatterns += [
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT,}),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)