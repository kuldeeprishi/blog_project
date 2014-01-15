from django.contrib import admin
from blog.models import Tag, Post, Comment
from django.forms import *
from django.db.models import *




class TagAdmin(admin.ModelAdmin):
	pass


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title', 'pub_date', 'status', 'featured', 'allow_comment')
	list_display_links = ["title",]
	list_editable = ['status', 'featured', 'allow_comment']
	search_fields = ('title', 'body')
	list_filter = ('pub_date',)
	prepopulated_fields = {'slug': ('title',)}
	ordering = ('-pub_date',)
	filter_horizontal = ('tags',)




class CommentAdmin(admin.ModelAdmin):
	pass




admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
