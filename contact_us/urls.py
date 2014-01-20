
from django.conf.urls import url,patterns
from django.http.response import HttpResponse




urlpatterns = patterns('contact_us.views',
                       url(r'^$','v_add_contact'),
                       #url(r'^$','v_test'),
                       #url(r'^test',lambda req:HttpResponse(req.POST.get('var','XXX'))),
                       )


    