from django.db import models
# from django.contrib.postgres.fields import JSONField
# Create your models here.
# from django.template.defaultfilters import slugify

class Shoes(models.Model):
	shoes_id		= models.IntegerField(primary_key=True)
    # category        = models.CharField(max_length=10, null=True, blank=True)
	brand 			= models.CharField(max_length=20)
	name 			= models.CharField(max_length=100)
	shoes_type		= models.CharField(max_length=30, null=True, blank=True)
	color			= models.CharField(max_length=40)
	price			= models.DecimalField(max_digits=5, decimal_places=2)
	price_before    = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	image           = models.FileField()
	# created 		= models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True)
	# updated 		= models.DateTimeField(auto_now_add=False, auto_now=True, null=True, blank=True)
	slug 			= models.CharField(max_length=200)



class Shoes_images(models.Model):
	shoes = models.ForeignKey(Shoes, on_delete = models.CASCADE)
	image = models.FileField()
class Shoes_360(models.Model):
	shoes = models.ForeignKey(Shoes, on_delete = models.CASCADE)
	image = models.FileField()

class Shoes_size(models.Model):
	shoes = models.ForeignKey(Shoes, on_delete = models.CASCADE)
	size  = models.CharField(max_length=15)
	stock = models.BooleanField()

class Post_cart(models.Model):
	shoes = models.ForeignKey(Shoes, on_delete = models.CASCADE)
	sessionid = models.CharField(max_length=40)
	size  = models.CharField(max_length=15)


	# def __unicode__(self):
	# 	return '%d: %s' % (self.stock, self.size)
