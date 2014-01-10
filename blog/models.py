import datetime
from time import time
from django.conf import settings
from django.core.urlresolvers import reverse

from django.db import models
from django.contrib.auth.models import User


# Generate timestamp based filename of uploaded articles
def get_upload_file_name(instance, filename):
	return 'uploaded_files/%s_%s'%(str(time()).replace('.','_'), filename)


class Tag(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name


STATUS_CHOICES = (
	('d', 'Draft'),
	('l', 'Live'),
)

class Post(models.Model):
	title = models.CharField(max_length=200, help_text='Give a Short and Meaningful Title')
	body = models.TextField(blank=True, null=True)
	image = models.FileField(upload_to=get_upload_file_name, default='', blank=True, null=True, help_text='\
		Post with Descriptive Image attract more Visitors.')
	pub_date = models.DateTimeField(default=datetime.datetime.now)
	last_modified = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='l')
	allow_comment = models.BooleanField(default=True, help_text='Allow Users to Comment on this Post?')
	featured = models.BooleanField(default=False, verbose_name="Featured Article", help_text='Check if this Post has to be Featured on Home Page!')
	tags = models.ManyToManyField(Tag, blank=True, null=True, help_text='Descriptive Tags let user search your article with ease.')
	slug = models.SlugField(max_length=20, unique=True, help_text="Slug Value is unique and generated automatically. If Slug error occur on save, please try to make it unique but keeping it meaningful.")

	class Meta:
		verbose_name_plural = ("Posts")
		ordering = ["-pub_date"]

	def __unicode__(self):
		return self.title


	@models.permalink
	def get_absolute_url(self):
		return ('post_entry_detail', (), {'year': self.pub_date.strftime("%Y"),
											'month': self.pub_date.strftime("%b").lower(),
											'day': self.pub_date.strftime("%d"),
											'slug': self.slug})

	
class Comment(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now=True)
	visible = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.user.username
