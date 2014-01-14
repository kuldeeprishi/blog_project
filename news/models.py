from django.db import models
from time import time

def get_upload_file_name(instance, filename):
        return 'uploaded_files/%s_%s'%(str(time()).replace('.','_'), filename)


STATUS=(('pub','published'),
	('draft','draft'))


class PublishedManager(models.Manager):
    def get_query_set(self):
        return super(PublishedManager, self).get_query_set().filter(status = "pub")


class News(models.Model):
    title=models.CharField(max_length=200 )
    image=models.ImageField(upload_to=get_upload_file_name,blank = True , null= True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS , default='pub')
    posted_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    get_published = PublishedManager()


    class Meta:
	verbose_name_plural = "News"
	ordering = ["-posted_on"]
	
    def __unicode__(self):
	    return self.title

    




# Create your models here.
