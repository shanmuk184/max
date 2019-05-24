from django.db import models

# Create your models here.
# ,,,,,,,,,,,,,,,

class articleModel(models.Model):
    job_id = models.IntegerField(blank=True, null=True)
    ns_category_id = models.IntegerField(blank=True, null=True)
    location_id = models.IntegerField(blank=True, null=True)
    job_type_id = models.IntegerField(blank=True, null=True)
    job_type = models.IntegerField(blank=True, null=True)
    _id = models.IntegerField(blank=True, null=True)
    filename = models.TextField(blank=True, null=True)
    job_title = models.TextField(blank=True, null=True)
    job_slug = models.TextField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)
    job_image = models.TextField(blank=True, null=True)
    job_status = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=60,blank=True, null=True)
    House_of = models.CharField(max_length=60,blank=True, null=True)
    Year = models.IntegerField(blank=True, null=True)
    epaper_link = models.URLField(blank=True, null=True)
    image_link = models.URLField(blank=True, null=True)
