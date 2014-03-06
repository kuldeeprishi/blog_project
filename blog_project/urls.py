from django.conf.urls import patterns, include, url
from auth import urls
from django.conf import settings
from django.http import HttpResponse
import base64
from django.views.generic import TemplateView
from django.conf.urls.static import static
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.site.urls
admin.autodiscover()


from .views import html

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog_project/', include('blog_project.foo.urls')),
    url('^accounts/profile/$', include('homepage.urls'), name='homepage'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^accounts/', include('allauth.urls')),
    url(r'^$', include('homepage.urls'), name='homepage'),
    # Uncomment the next line to enable the admin:
     url(r'^commnet/$', 'blog.views.comment',name="jbdk"),  
    # url(r'^auth/', include('auth.urls')),
    (r'^search/', include('haystack.urls')),
    (r'^tinymce/', include('tinymce.urls')),    
    url(r'^news/', include('news.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^team/$', lambda x: HttpResponse('''<!DOCTYPE HTML><html lang="en"> <head> <meta charset="utf-8"> <title> Meet the team </title> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <meta name="description" content=""> <meta name="author" content=""><!-- Styles --> <link href="/static/css/bootstrap2.css" rel="stylesheet" type="text/css"> <link href="/static/css/style.css" rel="stylesheet" type="text/css"> <link rel="\'stylesheet\'" id="\'prettyphoto-css\'" href="/static/css/prettyPhoto.css" type="\'text/css\'" media="\'all\'"> <link href="/static/css/fontello.css" type="text/css" rel="stylesheet"><!--[if lt IE 7]> <link href="css/fontello-ie7.css" type="text/css" rel="stylesheet"> <![endif]--><!-- Google Web fonts --> <link href="/'http://fonts.googleapis.com/css?family=Quattrocento:400,700/'" rel="\'stylesheet\'" type="\'text/css\'"> <link href="/'http://fonts.googleapis.com/css?family=Patua+One/'" rel="\'stylesheet\'" type="\'text/css\'"> <link href="/'http://fonts.googleapis.com/css?family=Open+Sans/'" rel="\'stylesheet\'" type="\'text/css\'"> <link href="/static/css/bootstrap-responsive2.css" rel="stylesheet" type="text/css"><!-- Le HTML5 shim, for IE6-8 support of HTML5 elements --><!--[if lt IE 9]> <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script> <![endif]--><!-- Favicon --><!-- JQuery --> <script type="text/javascript" src="/static/js/jquery.js"></script><!-- Load ScrollTo --> <script type="text/javascript" src="/static/js/jquery.scrollTo-1.4.2-min.js"></script><!-- Load LocalScroll --> <script type="text/javascript" src="/static/js/jquery.localscroll-1.2.7-min.js"></script><!-- prettyPhoto Initialization --> <script type="text/javascript" charset="utf-8"> $(document).ready(function(){ $("a[rel^=\'prettyPhoto\']").prettyPhoto(); }); </script> </head> <body> <!--******************** Team Section ********************--> <section id="team" class="single-page scrollblock"> <div class="container"> <h1> Meet the team </h1><!-- Five columns --> <div class="row"> <div class="span2"> <div class="teamalign"> <img class="team-thumb img-circle" src="/static/images/kuldeeprishi.jpeg" alt=""> </div> <h3> Kuldeep Rishi </h3> <div class="job-position"> Python/Django Developer </div> <div> kuldeepkrishi@gmail.com </div> </div><!-- ./span2 --> <div class="span2"> <div class="teamalign"> <img class="team-thumb img-circle" src="/static/images/irshad.jpg" alt=""> </div> <h3> Mohd. Irshad </h3> <div class="job-position"> Python/Django Developer </div> <div class="job-position"> mohdirshadmi4@gmail.com </div> </div> <div class="span2"> <div class="teamalign"> <img class="team-thumb img-circle" src="/static/images/irfan.jpg" alt=""> </div> <h3> Irfan Ansari </h3> <div class="job-position"> Python/Django Developer </div> <div class="job-position"> irfan.ansari.sga@gmail.com </div> </div> </div> </div><!-- /.container --> </section><!-- Loading the javaScript at the end of the page --><script type="text/javascript" src="/static/js/bootstrap.js"></script><script type="text/javascript" src="/static/js/jquery.prettyPhoto.js"></script><script type="text/javascript" src="/static/js/site.js"></script><!--ANALYTICS CODE--><script type="text/javascript">var _gaq = _gaq || []; _gaq.push([\'_setAccount\', \'UA-29231762-1\']); _gaq.push([\'_setDomainName\', \'dzyngiri.com\']); _gaq.push([\'_trackPageview\']); (function() { var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true; ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\'; var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s); })(); </script> </body></html>''')),

    url(r'^admin/', include(admin.site.urls)),  url(r'^admin/', include(admin.site.urls)),

    url(r'^newsletter/', include('newsletter.urls')),
    url(r'^subscribe', 'homepage.views.add_subscriber'),
    url(r'^activate/$', 'homepage.views.activate'),
    url(r'^imagefit/', include('imagefit.urls')),
    
    url(r'^about/', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^contactUS/', include('contact_us.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += urls.urlpatterns
