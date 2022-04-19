from django.db import models

# Create your models here.

class SystemUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,null=True,unique=True)
    email_id = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=20,null=True)

class ArtworkOrder(models.Model):
    customer_id	= models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=200,null=True)	
    email_id = models.CharField(max_length=200,null=True)	
    phone_number = models.CharField(max_length=20,null=True)	
    discount_rate = models.FloatField(null=True)
    order_date = models.DateField(null=True)
    approved_date = models.DateField(null=True)
    scheduled_print_date = models.DateField(null=True)	
    total_price	= models.FloatField(null=True)
    apparel_item = models.CharField(max_length=150,null=True)
    event_name = models.CharField(max_length=150,null=True)
    base_color	= models.CharField(max_length=50,null=True)
    theme_name	= models.CharField(max_length=150,null=True)
    max_colors	= models.CharField(max_length=150,null=True)
    art_location_01	= models.CharField(max_length=150,null=True)
    description_01 = models.CharField(max_length=1000,null=True)
    cost_01	= models.IntegerField(null=True)
    employee_01	= models.CharField(max_length=150,null=True)
    complete_date_01 = models.DateField(null=True)
    colors_01 = models.CharField(max_length=150,null=True)
    art_location_02	= models.CharField(max_length=150,blank=True,null=True)
    description_02	= models.CharField(max_length=1000,blank=True,null=True)
    cost_02	= models.IntegerField(blank=True,null=True)
    employee_02	= models.CharField(max_length=150,blank=True,null=True)
    complete_date_02 = models.DateField(blank=True,null=True)
    colors_02 = models.CharField(max_length=150,blank=True,null=True)