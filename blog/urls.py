from django.conf.urls import patterns, include, url

from django.conf.urls import *
from django.conf import settings
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView, DayArchiveView, DateDetailView
from blog.models import Post

post_info_dict = {
	'model': Post,
	'date_field': 'pub_date',
	'paginate_by': 10,
	'template_name': 'blog/display_object_list.html',
}

urlpatterns = patterns('',
    url(r'^$', ArchiveIndexView.as_view(**post_info_dict), name='post_archive_index'),
    url(r'^(?P<year>\d{4})/$', YearArchiveView.as_view(make_object_list = True, allow_future = True, **post_info_dict), name='post_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', MonthArchiveView.as_view(**post_info_dict), name='post_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', DayArchiveView.as_view(**post_info_dict), name='post_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', DateDetailView.as_view(model=Post, date_field='pub_date'), name='post_entry_detail'),
    url(r'^tag/(?P<tag>[-\w]+)/$', 'blog.views.get_blog_by_tag', name='blog_by_tag'),
    url(r'detail/(?P<post_id>\d+)/$','blog.views.detail_view', name="get_post_detail")
   
)
<<<<<<< HEAD

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
=======
>>>>>>> 8ae2b46b8a6cc863ee65e34d0097d7711b4f7a05
