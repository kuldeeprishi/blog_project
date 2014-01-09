from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    #
     url(r'^$', 'blog.views.post_view', name='home'),
     url(r'detail/(?P<post_id>\d+)/$', 'blog.views.detail_view', name='detail'),

     
)
  
