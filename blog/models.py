from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name

STATUS_CHOICES = (
	('d', 'Draft'),
	('l', 'Live'),
)

class Post(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField(blank=True, null=True)
	image = models.ImageField(upload_to='media/uploads', blank=True, null=True)
	pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')
	last_modified = models.DateTimeField(auto_now=True)
	allow_comment = models.BooleanField(default=True)
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='l')
	featured = models.BooleanField(default=False, verbose_name="Featured Article")
	tags = models.ManyToManyField(Tag, blank=True, null=True)
	slug = models.SlugField(max_length=20)

	def __unicode__(self):
		return self.title

	
class Comment(models.Model):
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)
	body = models.TextField()
	pub_date = models.DateTimeField(auto_now=True)
	visible = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.user.username
