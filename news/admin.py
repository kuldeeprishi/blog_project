from django.contrib import admin
from .models import News
from django.db.models import *
from tinymce.widgets import TinyMCE

class NewsForm(forms.ModelForm):

    class Meta:
        model = News

    class Media:
            js = (
                     settings.STATIC_URL + 'customtiny.js',
		     settings.STATIC_URL + 'tiny_mce/tiny_mce_src.js',		
		     settings.STATIC_URL + 'tiny_mce/tiny_mce.js',
	
            ) 


class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    date_hierarchy = 'posted_on'
    list_display = ('title', 'posted_on')
    search_fields = ('title',)
    list_filter = ('posted_on',) 
    ordering = ('-posted_on',)
admin.site.register(News , NewsAdmin)

