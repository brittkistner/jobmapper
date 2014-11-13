import json
import urllib
from django.db import models

class LinkedIn(models.Model):
    LICID = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField()
    latitude = models.DecimalField(max_digits=18, null=True, blank=True)
    longitude = models.DecimalField(max_digits=18, null=True, blank=True)
    twitter = models.CharField(max_length=15)
    logo_url = models.URLField()
    description = models.TextField()
    company_type = models.CharField(max_length=75)
    industry = models.CharField(max_length=255) #there can be more than one
    #specialties (go in keywords, think about the keywords)
    company_size = models.IntegerField()
    tckr = models.CharField(max_length=10)
    founded_year = models.IntegerField()
    website_url = models.URLField()
    employee_count_range = models.IntegerField()

    def __unicode__(self):
        return u"LinkedIn: {}".format(self.name)

#REVIEW THIS
    def geocode(self, location):
        location = urllib.quote_plus(location)
        request = "http://maps.googleapis.com/maps/api/geocode/json?address={}&sensor=false".format(location)
        data = json.loads(urllib.urlopen(request).read())

        if data['status'] == 'OK':
            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            return latitude, longitude

class GlassDoorCEO(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    number_ratings = models.IntegerField()
    pct_approve = models.FloatField()
    pct_disapprove = models.FloatField

    def __unicode__(self):
        return u"{}".format(self.name)

class GlassDoor(models.Model):
    GDCID = models.CharField(max_length=10, primary_key=True)
    asin = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=255)
    overall_rating = models.FloatField() #make sure to change these from string to float
    rating_description = models.CharField(max_length=50)
    culture_values_rating = models.FloatField()
    senior_leadership_rating = models.FloatField()
    compensation_benefits_rating = models.FloatField()
    career_opportunities_rating = models.FloatField()
    work_life_balance_rating = models.FloatField()
    website_url = models.URLField()
    number_ratings = models.IntegerField()
    logo_url = models.URLField()
    ceo = models.ForeignKey(GlassDoorCEO, related_name="company")

    def __unicode__(self):
        return u"Glassdoor: {}".format(self.name)
# through table?? for the Mapping Table

class Company(models.Model):
    pass

    # def __unicode__(self):
    #         return u"{}".format(self.name)

class Keyword(models.Model):
    word = models.CharField(max_length=75)
    companies = models.ManyToManyField(Company, related_name="keywords")

    def __unicode__(self):
        return u"{}".format(self.word)