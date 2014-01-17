
from django.conf.urls import url,patterns



urlpatterns = patterns('contact_us.views',
                       url(r'^$','v_add_contact'),
                       )
                    