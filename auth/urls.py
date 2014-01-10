
from django.conf.urls import patterns,url


urlpatterns = patterns('auth.views.authenticate',
    url(r'^$','v_home'),
    url(r'^login/$','v_login'),
    url(r'^logout/$','v_logout'),
    url(r'^forgotPassword/$','v_forgotPassword'),
    url(r'^resetPassword/$','v_resetPassword'),      
 
)